#!/usr/bin/python

from scrapy import Selector

body = '<html><head><title>Hello,World</title></head></body></html>'

selector = Selector(text=body)

title = selector.xpath('//title/text()').extract_first()

print(title)


