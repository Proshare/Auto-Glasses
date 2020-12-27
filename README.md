配置需求window10+python3.6以上+vs2017+opencv+pycharm
下面是windows10 笔记本的配置截图，如果是macOS原则需要的库是相同的。也就是这些库是必须要安装。

库安装注意事项：
1、切记安装一定要对应python版本号，建议python3.6以上，下面是安装教程。

https://blog.csdn.net/u012325865/article/details/83961127
2、由于在安装python版本的opencv支持库回遇到版本以及32位64位的问题，需要自己去寻找python版本的.whl下载.下面的地址是各种whl网址
https://www.lfd.uci.edu/~gohlke/pythonlibs/
上面网址详细说明了whl的库文件如何使用。
https://blog.csdn.net/weixin_38168838/article/details/99738371?utm_medium=distribute.pc_relevant.none-task-blog-baidujs_title-11&spm=1001.2101.3001.4242
3、cmake与dlib安装比较复杂，这两个库是必须要安装的，且需要支持的环境，而且由于windows系统并不集成vs相关库而opencv却又是需要安装vs库，所以建议直接下菜vs2017版本。下面网址会详细描述。
https://www.cnblogs.com/wdzn/p/9675821.html
4、待各种库文件安装完毕需要执行realtime_liu即可进行视频实时换眼镜，这里在弹出框里进行按键操作，d按键代表开始，c按键代表替换眼镜，q按键代表退出程序。

