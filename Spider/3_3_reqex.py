#!/usr/bin/python

import re

html = '''<div id="songs-list">
    <h2 class="title">经典老歌</h2>
    <p class="introduction">
        经典老歌列表
    </p>
    <ul id="list" class="list-group">
        <li data-view="2">一路上有你</li>
        <li data-view="7">
            <a href="/2.mp3" singer="任贤齐">沧海一声笑</a>
        </li>
        <li data-view="4" class="active">
            <a href="/3.mp3" singer="齐秦">往事随风</a>
        </li>
        <li data-view="6"><a href="/4.mp3" singer="beyond">光辉岁月</a></li>
        <li data-view="5"><a href="/5.mp3" singer="陈慧琳">记事本</a></li>
        <li data-view="5">
            <a href="/6.mp3" singer="邓丽君"><i class="fa fa-user"></i>但愿人长久</a>
        </li>
    </ul>
</div>'''
results = re.findall('<l(?:i).*?>(.*?)</li>',html,re.S)

#results = re.findall('<li.*?>\s*?(<a.*?>)?(\w+)(</a>)?\s*?</li>',html,re.S)
#html = re.sub('<a.*?>|</a>','',html)
#results = re.findall('<l(?:i).*?>(.*?)</li>',html,re.S)
#for result in results:
#    print(result.strip())
#import requests
#
#import re
#content = 'hello 123 4567 World_This is a Regex Demo'
#
#print(len(content))
#print(content)
#
##result = re.match('^hello\s\d\d\d\s(\d+)\s\w{10}',content)
#result = re.match('^hello(.*)$',content)
#print(result)
#
#print(result.group())
#print(result.span())
#

#import re
#
#content = 'Extra stings Hello 1234567 World_This is a Regex Demo Extra stings'
#
#result = re.search('Hello.*?(\d+).*?Demo',content)
#print(result)