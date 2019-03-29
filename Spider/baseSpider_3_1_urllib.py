#!/usr/bin/python
#from urllib import request,parse
from urllib.robotparser import RobotFileParser

from urllib.request import urlopen

#url = 'http://www.jianshu.com/'
#
#headers = {
#    'User-Agent':'Mozilla/4.0 (compatible;MSIE 5.5;Windows NT)',
#    'Host':'jianshu.com'
#}
#dict = {
#    'name':'Germey'
#}
#
#data = bytes(parse.urlencode(dict),encoding='utf-8')
#req = request.Request(url = url,headers = headers,method = 'GET')
#response = request.urlopen(req)
#print(response.read().decode('utf-8'))
#
#rp = RobotFileParser()
#rp.parse(response.read().decode('utf-8').split('\n'))

rp = RobotFileParser()
rp.set_url('file:///Spider/robots')
rp.read()
print(rp)
print(rp.can_fetch('*','https://www.jianshu.com/p/a91cb8a2e55d'))
print(rp.can_fetch('*',"http://www.jianshu.com/search?q=python&page=1&type=collections"))


#from urllib.parse import unquote
#
#url = 'https://www.baidu.com/s?wd=%E5%A3%81%E7%BA%B8'
#print(unquote(url))
#from urllib.parse import urlencode
#from urllib.parse import parse_qsl
#from urllib.parse import quote
#
#keyword = '壁纸'
#url = 'https://www.baidu.com/s?wd=' + quote(keyword)
#
#print(url)
#query = 'name=gemey&age=22'
#print(parse_qsl(query))

#params = {
#    'name':'germey',
#    'age':22
#}
#base_url='http://www.baidu.com?'
#url = base_url + urlencode(params)
#print(url)
#from urllib.parse import urlunparse

#data = ['http','www.baidu.com','index.html','user','a=6','commnet']
#print(urlunparse(data))

#from urllib.parse import urlunsplit
 
#data = ['http','www.baidu.com','index.html;user','a=6','commnet']
#print(urlunsplit(data))
#from urllib.parse import urlsplit

#from urllib.parse import urljoin
#
#print(urljoin('http://www.baidu.com','FAQ.html'))
#print(urljoin('http://www.baidu.com','https://cuiqingcai.com/FAQ.html'))
#print(urljoin('http://www.baidu.com/about.html','https://cuiqingcai.com/FAQ.html'))
#print(urljoin('http://www.baidu.com/about.html','https://cuiqingcai.com/FAQ.html?question=2'))
#print(urljoin('http://www.baidu.com?wb=abc','https://cuiqingcai.com/index.php'))
#print(urljoin('http://www.baidu.com','?category=2#comment'))
#print(urljoin('www.baidu.com','?category=2#comment'))
#print(urljoin('www.baidu.com#comment','?category=2'))
#result = urlsplit('http://www.baidu.com/index.html;user?id=5#comment')
#print(result)
#print(type(result),result)
#print(result.scheme,result[0],result.netloc,result[1],sep='\n')

#import socket
#import urllib.request
#import urllib.error
#
#try:
#    response = urllib.request.urlopen('https://www.baidu.com',timeout=0.001)
#except urllib.error.URLError as e:
#    print(type(e.reason))
#    if isinstance(e.reason,socket.timeout):
#        print('TIME OUT')

#from urllib import request,error
#
#try:
#    response = request.urlopen('https://cuiqingcai.com/index.html')
#except error.HTTPError as e:
#    print(e.reason,e.code,e.headers,sep='\n')
#except error.URLError as e:
#    print(e.reason)
#else:
#    print('Request Successfully')
#
#try:
#    response = request.urlopen('https://cuiqingcai.com/index.html')
#except error.URLError as e:
#    print(e.reason)

#from urllib import request,error
#try:
#    response = request.urlopen('http://cuiqingcai.com/index.html')
#except error.HTTPError as e:
#    print(e.reason,e.code,e.headers,sep='\n')
#import http.cookiejar,urllib.request
#
##filename = 'cookies.txt'
#cookie = http.cookiejar.LWPCookieJar()
#cookie.load('cookies.txt',ignore_discard=True,ignore_expires=True)
#
#handler = urllib.request.HTTPCookieProcessor(cookie)
#opener = urllib.request.build_opener(handler)
#
#response = opener.open('http://www.baidu.com/')
#print(response.read().decode('utf-8'))
#for item in cookie:
#    print(item.name + "=" + item.value)
#cookie.save(ignore_discard=True,ignore_expires=True)

#from urllib.error import URLError
#from urllib.request import ProxyHandler,build_opener
#
#proxy_handler = ProxyHandler({
#    'http':'http://192.168.86.26:18888'
#})
#opener = build_opener(proxy_handler)
#
#try:
#    response = opener.open('http://www.baidu.com')
#    print(response.read().decode('utf-8'))
#except URLError as e:
#    print(e.reason)
#from urllib.request import HTTPPasswordMgrWithDefaultRealm,HTTPBasicAuthHandler,build_opener
#from urllib.error import URLError
#
#username = 'admin'
#password = '1qaz#EDC'
#url = 'http://localhost:6801'
#
#p = HTTPPasswordMgrWithDefaultRealm()
#p.add_password(None,url,username,password)
#auth_header = HTTPBasicAuthHandler(p)
#opener = build_opener(auth_header)
#
#try:
#    result = opener.open(url)
#    html = result.read().decode('utf-8')
#    print(html)
#except URLError as e:
#    print(e.reason)
#from urllib import request,parse
#
#url = 'http://httpbin.org/post'
#
#headers = {
#    'User-Agent':'Mozilla/4.0 (compatible;MSIE 5.5;Windows NT)',
#    'Host':'httpbin.org'
#}
#dict = {
#    'name':'Germey'
#}
#
#data = bytes(parse.urlencode(dict),encoding='utf-8')
#req = request.Request(url = url,data = data,headers = headers,method = 'POST')
#response = request.urlopen(req)
#print(response.read().decode('utf-8'))

#import urllib.parse
#import socket
#import urllib.request
#import urllib.error
#
#request = urllib.request.Request('http://python.org')
#response = urllib.request.urlopen(request)
#print(response.read().decode('utf-8'))


#try:
#    response = urllib.request.urlopen('http://httpbin.org/get',timeout=0.001)
#except urllib.error.URLError as e:
#    if isinstance(e.reason,socket.timeout):
#        print(e.reason)
#        print('TIME OUT')

#data = bytes(urllib.parse.urlencode({'word':'hello'}),encoding='utf-8')
#response = urllib.request.urlopen('http://httpbin.org/post',data=data)
#print(response.read().decode('utf-8'))

#response = urllib.request.urlopen('https://www.python.org')
#print(type(response))
#print(response.read().decode('utf-8'))
#print(response.status)
#print(response.getheaders())
#print(response.getheader('Server'))

