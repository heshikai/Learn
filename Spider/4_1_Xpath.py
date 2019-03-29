#!/usr/bin/python

#from lxml import etree
#text = '''
#<div>
#    <ul>
#         <li class="item-0"><a href="link1.html">first item</a></li>
#         <li class="item-1"><a href="link2.html">second item</a></li>
#         <li class="item-inactive"><a href="link3.html">third item</a></li>
#         <li class="item-1"><a href="link4.html">fourth item</a></li>
#         <li class="item-0"><a href="link5.html">fifth item</a>
#     </ul>
# </div>
#'''
#html = etree.HTML(text)
#result = etree.tostring(html)
#print(result.decode('utf-8'))
#from lxml import etree

#html = etree.parse('./test.html',etree.HTMLParser())
#print(etree.tostring(html).decode('utf-8'))

#html = etree.parse('./test.html',etree.HTMLParser())
#result = html.xpath('//a[@href="link4.html"]/parent::*/@class')
#result = html.xpath('//li[@class="item-0"]//text()')
#result = html.xpath('//li/@class')
#for result_line in result:
#    print(result_line)


from lxml import etree
#text = '''
#<li class="li li-first" name="item"><a href="link.html">first item</a></li>
#'''
#html = etree.HTML(text)
html = etree.parse('./test.html',etree.HTMLParser())

#result = html.xpath('//li[contains(@class,"item-0-1")]/a/text()')
#result = html.xpath('//li[contains(@class,"li") and @name="item"]/a/text()')
#result = html.xpath('//li[1]/a/text()')
#print(1)
#[print(result_line) for result_line in result]
#   
#result = html.xpath('//li[last()]/a/text()')
#print(2)
#[print(result_line) for result_line in result]
#
#result = html.xpath('//li[position()<=3]/a/text()')
#print(3)
#[print(result_line) for result_line in result]
#
#result = html.xpath('//li[last()-2]/a/text()')
#print(4)
#[print(result_line) for result_line in result]

result = html.xpath('//li[1]/ancestor::*')
print(1)
[print(result_line) for result_line in result]
   
result = html.xpath('//li[1]/ancestor::div')
print(2)
[print(result_line) for result_line in result]

result = html.xpath('//li[1]/attribute::*')
print(3)
[print(result_line) for result_line in result]

result = html.xpath('//li[1]/child::a[@href="link1.html"]')
print(4)
[print(result_line) for result_line in result]

result = html.xpath('//li[1]/descendant::span')
print(5)
[print(result_line) for result_line in result]

result = html.xpath('//li[1]/following::*[2]')
print(6)
[print(result_line) for result_line in result]

result = html.xpath('//li[1]/following-sibling::*')
print(7)
[print(result_line) for result_line in result]
