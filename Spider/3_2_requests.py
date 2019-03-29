#!/usr/bin/python

from requests import Request,Session

url = 'http://httpbin.org/post'
data = {'name':'germey'}
headers = { 
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) \
                    AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.80 Safari/537.36'
}
s = Session()
req = Request('POST',url,data = data,headers = headers)
prepared = s.prepare_request(req)
r = s.send(prepared)
print(r.text)
#import requests


#from requests_oauthlib import OAuth1

#url = 'https://api.twitter.com/1.1/account/verify_credentials.json'
#auth = OAuth1('YOUR_APP_KEY',
#              'YOUR_APP_SECRET',
#              'USER_OAUTH_TOKEN',
#              'USER_OAUTH_TOKEN_SECRET')
#requests.get(url,auth=auth)



#import requests
#
#from requests.auth import HTTPBasicAuth
#
#r = requests.get('http://192.168.86.26:6801',auth=HTTPBasicAuth('admin','1qaz#EDC'))
#
#print(r.text)
#proxies = {
#    "http":"http://192.168.86.26:18888/",
#}
#
#headers = { 
#    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) \
#                    AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.80 Safari/537.36'
#}
#
#r = requests.get("http://www.zhihu.com",proxies = proxies,timeout = 3,headers = headers)
#
#print(r.text)


#import requests
#
#s = requests.session()
#s.get('http://httpbin.org/cookies/set/number/12345678')
#
#r = s.get('http://httpbin.org/cookies')
#print(r.text)
#import requests
#response = requests.get('http://www.12306.cn')
#print(response.status_code)
#import requests
#files = {'file':open('favicon.ico','rb')}
#r=requests.post("http://httpbin.org/post",files=files)
#print(r.text)

#import requests
#
#r = requests.get("https://www.baidu.com")
#print(r.cookies)
#
#for key,value in r.cookies.items():
#    print(key + '=' + value)
#import requests
#
#cookies = 'zap=07ae3c9c-b073-4cbc-bef9-d5f34eb0162b; __DAYU_PP=Bi22ImuUjf6AfvJjquYI2db6d107f02d; d_c0="AGBjOdMQow2PTjKnTEeCT2p8gi_OvIy74v0=|1527061454"; _xsrf=ZAQeLMwtedRCS3lhalY5IJueLCAGdSky; l_n_c=1; q_c1=576410d45bf44b3da7367bcf81fedcc8|1544603283000|1533202201000; n_c=1; __utmc=51854390; l_cap_id="MzBmNTAyM2U5MTBkNDNiMmFlMTY4NDRkMTY1YmE1Zjk=|1544604223|457c2bdf8cc4639db9a525d8641087da120f805b"; r_cap_id="ZTQ2NWFkZjE2NzlkNDY3NDkzYWMzZjhjMmM1OWEzMWY=|1544604223|8e6b7bd5d59d25e6bb11e7378f5073c6d4f673c6"; cap_id="MDZkOWEzOTBiMTgzNDFmNDhiZDFmNWMwOWU5Y2Q1MjQ=|1544604223|18954cdcf244b0fd3a730d04de868c217271dcf1"; capsion_ticket="2|1:0|10:1544606755|14:capsion_ticket|44:YzZhZmE3MDdhOGU3NGYwNGIwMmZmZjMyZjEzZWUzMmI=|31f312d910d3e5d85dc84c7643bbd638e2242e379c68bc325c71e52aa5d48454"; z_c0="2|1:0|10:1544606763|4:z_c0|92:Mi4xaW5RbUJBQUFBQUFBWUdNNTB4Q2pEU1lBQUFCZ0FsVk5LeUwtWEFCT1J2MWRSbC1zWjVzMUZudmRJdEpod0s2TXRR|627f8f2275824fc3c644e4e06d9ab158db2437f948479d8b5e17179e44a277b7"; tst=r; __utma=51854390.1519965851.1544603276.1544603276.1544606851.2; __utmb=51854390.0.10.1544606851; __utmz=51854390.1544606851.2.2.utmcsr=zhihu.com|utmccn=(referral)|utmcmd=referral|utmcct=/people/edit; __utmv=51854390.100--|2=registration_date=20170216=1^3=entry_date=20170216=1; tgw_l7_route=7139e401481ef2f46ce98b22af4f4bed'
#
#jar = requests.cookies.RequestsCookieJar()
#headers = { 
#    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) \
#                    AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.80 Safari/537.36',
#    'Host':'www.zhihu.com'
#}
#for cookie in cookies.split(';'):
#    key,value = cookie.split('=',1)
#    jar.set(key,value)
#    
#r = requests.get('https://www.zhihu.com',cookies=jar,headers = headers)
#print(r.text)
#import requests
#headers = { 
#    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) \
#                    AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.80 Safari/537.36',
#    'Host':'www.zhihu.com',
#    'Cookie':'zap=07ae3c9c-b073-4cbc-bef9-d5f34eb0162b; __DAYU_PP=Bi22ImuUjf6AfvJjquYI2db6d107f02d; d_c0="AGBjOdMQow2PTjKnTEeCT2p8gi_OvIy74v0=|1527061454"; _xsrf=ZAQeLMwtedRCS3lhalY5IJueLCAGdSky; l_n_c=1; q_c1=576410d45bf44b3da7367bcf81fedcc8|1544603283000|1533202201000; n_c=1; __utmc=51854390; l_cap_id="MzBmNTAyM2U5MTBkNDNiMmFlMTY4NDRkMTY1YmE1Zjk=|1544604223|457c2bdf8cc4639db9a525d8641087da120f805b"; r_cap_id="ZTQ2NWFkZjE2NzlkNDY3NDkzYWMzZjhjMmM1OWEzMWY=|1544604223|8e6b7bd5d59d25e6bb11e7378f5073c6d4f673c6"; cap_id="MDZkOWEzOTBiMTgzNDFmNDhiZDFmNWMwOWU5Y2Q1MjQ=|1544604223|18954cdcf244b0fd3a730d04de868c217271dcf1"; capsion_ticket="2|1:0|10:1544606755|14:capsion_ticket|44:YzZhZmE3MDdhOGU3NGYwNGIwMmZmZjMyZjEzZWUzMmI=|31f312d910d3e5d85dc84c7643bbd638e2242e379c68bc325c71e52aa5d48454"; z_c0="2|1:0|10:1544606763|4:z_c0|92:Mi4xaW5RbUJBQUFBQUFBWUdNNTB4Q2pEU1lBQUFCZ0FsVk5LeUwtWEFCT1J2MWRSbC1zWjVzMUZudmRJdEpod0s2TXRR|627f8f2275824fc3c644e4e06d9ab158db2437f948479d8b5e17179e44a277b7"; tst=r; __utma=51854390.1519965851.1544603276.1544603276.1544606851.2; __utmb=51854390.0.10.1544606851; __utmz=51854390.1544606851.2.2.utmcsr=zhihu.com|utmccn=(referral)|utmcmd=referral|utmcct=/people/edit; __utmv=51854390.100--|2=registration_date=20170216=1^3=entry_date=20170216=1; tgw_l7_route=7139e401481ef2f46ce98b22af4f4bed'
#}
#r = requests.get('https://www.zhihu.com',headers = headers)
#print('\n'.join(   r.text.split('\\n')  )  )
#headers = {
#    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) \
#                    AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.80 Safari/537.36'
#}



#r = requests.get('http://www.jianshu.com/robots.txt',headers=headers)


#print(r.status_code)
#exit() if not r.status_code == requests.codes.ok else print('Request Successfullly')

#import requests
#r = requests.get('http://www.jianshu.com')
#print(type(r.status_code),r.status_code)
#print(type(r.headers),r.headers)
#
#print(type(r.cookies),r.cookies)
#print(type(r.url),r.url)
#print(type(r.history),r.history)

#import requests
#data = {
#    'name':'germey',
#    'age':22
#}
#r = requests.post("http://httpbin.org/post",data = data)
#print(r.text)
#import requests
#
#r = requests.get("http://github.com/favicon.ico")
#print(r.text)
#print(r.content)

#import requests
#r = requests.get("http://github.com/favicon.ico")
#with open('favicon.ico','wb') as f:
#    f.write(r.content)

#import requests
#headers = {
#    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) \
#                    AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.80 Safari/537.36'
#}
#r = requests.get("https://www.zhihu.com/explore",headers = headers)
#print(r.text)
#import requests
#import re
#
#headers = {
#    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) \
#                    AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.80 Safari/537.36'
#}
#r = requests.get("https://www.zhihu.com/explore",headers=headers)
#pattern = re.compile('explore-feed.*?question_link.*?>(.*?)</a>',re.S)
#print(re.findall(pattern,r.text))
#data = {
#    'name':'germey',
#    'age':22,
#    'sex':'male'
#}
#r = requests.get('http://httpbin.org/get',params=data)
#print(type(r.text))
#print(r.json())
#print(type(r.json()))

#r = requests.get('https://www.baidu.com')
#
#print(type(r))
#print(r.status_code)
#print(type(r.text))
#print(r.text)
#print(r.cookies)

#r = requests.post('http://httpbin.org/post')
#r = requests.put('http://httpbin.org/put')
#r = requests.delete('http://httpbin.org/delete')
#r = requests.head('http://httpbin.org/head')
#r = requests.options('http://httpbin.org/options')
