# Spider

学习python3 爬虫 代码 实战以及心得

参考书籍《python3 网络爬虫开发实战》 2018年4月第1版 崔庆才


巨坑：
1.windows下安装pip install tesserocr
这个会失败，原因如下：
执行此命令后，会直接去https://pypi.org/下载tesserocr的源码，然后编译安装。
在windows下，自动编译会出各种类型的错误，解决完一个又是另外一个。
正确的方式是到github上下载对应环境的release版本，然后pip install xxxx.whl就能成功。
https://github.com/simonflueckiger/tesserocr-windows_build/releases

普坑：
1.
    www.janshu.com/robots.txt用文中例子并不能正确获取，需要用浏览器将这个文件下载到本地，然后再set_url处改为本地路径来解决。
13.2
    11. scrapy crawl quotes时应重启数据库 systemctl restart mongod




常用：
需要用用户名登录时
scrapyd > /dev/null &
nginx -c  /etc/nginx/nginx.conf
nginx -s reload 
http://192.168.86.26:6801/

