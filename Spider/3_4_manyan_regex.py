#!/usr/bin/python

import requests
import re
import json
import time

headers = { 
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) \
                    AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.80 Safari/537.36'
}

offset = 0 
items = []

while(offset < 100 ):
    time.sleep(0.1)
    result = requests.get('https://maoyan.com/board/4?offset=' + str(offset),headers=headers)

    movies_match_pattern = re.compile('<dd>\
.*?board-index.*?>(\d+).\
*?title="(.*?)"\
.*?主演：(\S*?)\s.\
*?上映时间：(\d{4}-\d{2}-\d{2})\
'
                            ,re.S)

    movies_matches = re.findall(movies_match_pattern,result.text)

    for movie in movies_matches:
        print(movie[0],'{:<25}'.format(movie[1]),movie[2],movie[3],sep='\t')
        items.append({
            'rank':movie[0],
            'name':movie[1],
            'actors':movie[2],
            'date':movie[3],
        })
    offset += 10
#print(result.text)

with open('result_maoyan_top100.txt','a',encoding='utf-8') as f:
    for item in iter(items):
        f.write(json.dumps(item,ensure_ascii=False)+'\n')
        
