import dlib
from PIL import Image, ImageDraw, ImageFont
import random

import cv2

from imutils.video import VideoStream
from imutils import face_utils, translate, rotate, resize

import numpy as np

vs = VideoStream().start()

detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor('shape_predictor_68_face_landmarks.dat')

max_width = 500
frame = vs.read()
frame = resize(frame, width=max_width)

fps = vs.stream.get(cv2.CAP_PROP_FPS) # need this for animating proper duration

animation_length = fps * 5
current_animation = 0
glasses_on = fps * 3

# uncomment for fullscreen, remember 'q' to quit
# cv2.namedWindow('deal generator', cv2.WND_PROP_FULLSCREEN)
#cv2.setWindowProperty('deal generator', cv2.WND_PROP_FULLSCREEN,
#                          cv2.WINDOW_FULLSCREEN)

deal = Image.open("./Glasses/0.png")


dealing = False
number =0
while True:
    frame = vs.read()
    frame = resize(frame, width=max_width)
    img_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = []

    rects = detector(img_gray, 0)
    img = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
    # print(rects)
    for rect in rects:
        face = {}
        shades_width = rect.right() - rect.left()

        # predictor used to detect orientation in place where current face is
        shape = predictor(img_gray, rect)
        shape = face_utils.shape_to_np(shape)

        # grab the outlines of each eye from the input image
        leftEye = shape[36:42]
        rightEye = shape[42:48]

        # compute the center of mass for each eye
        leftEyeCenter = leftEye.mean(axis=0).astype("int")
        rightEyeCenter = rightEye.mean(axis=0).astype("int")

	    # compute the angle between the eye centroids
        dY = leftEyeCenter[1] - rightEyeCenter[1]
        dX = leftEyeCenter[0] - rightEyeCenter[0]
        angle = np.rad2deg(np.arctan2(dY, dX)) 
        # print((shades_width, int(shades_width * deal.size[1] / deal.size[0])))
        # 图片重写
        current_deal = deal.resize((shades_width, int(shades_width * deal.size[1] / deal.size[0])),
                               resample=Image.LANCZOS)
        current_deal = current_deal.rotate(angle, expand=True)
        current_deal = current_deal.transpose(Image.FLIP_TOP_BOTTOM)

        face['glasses_image'] = current_deal
        left_eye_x = leftEye[0,0] - shades_width // 4
        left_eye_y = leftEye[0,1] - shades_width // 6
        face['final_pos'] = (left_eye_x, left_eye_y)

        # I got lazy, didn't want to bother with transparent pngs in opencv
        # this is probably slower than it should be
        # 图片动画以及配置
        if dealing:
            # print("current_y",int(current_animation / glasses_on * left_eye_y))
            if current_animation < glasses_on:
                current_y = int(current_animation / glasses_on * left_eye_y)
                img.paste(current_deal, (left_eye_x, current_y-20), current_deal)
            else:
                img.paste(current_deal, (left_eye_x, left_eye_y-20), current_deal)
                # img.paste(text, (75, img.height // 2 - 52), text)

    # 起初动画配置
    if dealing:
        current_animation += 1
        frame = cv2.cvtColor(np.asarray(img), cv2.COLOR_RGB2BGR)
    # 按键选择
    cv2.imshow("deal generator", frame)
    key = cv2.waitKey(1) & 0xFF
    #退出程序
    if key == ord("q"):
        break
    # 开始程序
    if key == ord("d"):
        dealing = not dealing
    # 图片切换
    if key == ord("c"):
        # 让图片从上面重新开始
        # current_animation = 0

        number = str(random.randint(0, 8))
        print(number)
        deal = Image.open("./Glasses/"+number+".png")
cv2.destroyAllWindows()
vs.stop()
