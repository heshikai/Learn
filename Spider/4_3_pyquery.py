#!/usr/bin/python


#html = '''
#<div>
#    <ul>
#         <li class="item-0">first item</li>
#         <li class="item-1"><a href="link2.html">second item</a></li>
#         <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
#         <li class="item-1 active"><a href="link4.html">fourth item</a></li>
#         <li class="item-0"><a href="link5.html">fifth item</a></li>
#     </ul>
# </div>
#'''
#
#from pyquery import PyQuery as pq
#
#doc = pq(html)
#print(doc('li'))


html = '''
<div id="container">
    <ul class="list">
         <li class="item-0">first item</li>
         <li class="item-1 inactive"><a href="link2.html">second item</a></li>
         <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
         <li class="item-1 active"><a href="link4.html">fourth item</a></li>
         <li class="item-0"><a href="link5.html">fifth item</a></li>
     </ul>
     <p> hello,pyquery</p>
     <p> hello, this is second sibling</p>
 </div>
'''

from pyquery import PyQuery as pq
doc = pq((html))

print(doc('#container .list li'))
print(type(doc('#container .list li')))

items = doc('.list')
print(type(items))
print(items)

lis = items.children()
print(type(lis))
print(lis)
lis = items.parents()
print(type(lis))
print(lis)
lis = items.siblings()
print(type(lis))
print(lis)

print("============")

li = doc('.item-0.active')
print(li)
print(str(li))
#lis = items.find('li')
#print(type(lis))
#print(lis)


#doc = pq(url='https://cuiqingcai.com')
#print(doc('title'))

print("============")

lis = doc('li').items()
print(type(lis))
[print(li,type(li)) for li in lis]

print("======================================")

a = doc('.item-0.active a')
print(a,type(a))
print(a.attr('href'))
print(a.text())
for attr in a.items():
    print('-------------------------')
    print(attr,attr.attr('href'))


print("======================================")
a = doc('.item-0.active')
print(a)
print(a.html())

print("======================================")
a = doc('.active')
print(a)
print(a.html())
print(a.text())

print("======================================")

li = doc('.item-0.active')
print(li)
li.removeClass('active')
print(li)
li.addClass('active')
print(li)

print("======================================")

li = doc('.item-0.active')
print(li)

li.attr('name','link')
print(li)
li.text('changed itme')
print(li)
li.html('<span>changed item</span>')
print(li)

print("======================================")


html = '''
<div class="wrap">
    Hello, World
    <p>This is a paragraph.</p>
 </div>
'''
from pyquery import PyQuery as pq
doc = pq(html)

wrap = doc('.wrap')
wrap.find('p').remove()
print(wrap.text())


print('====================================')


html = '''
<div class="wrap">
    <div id="container">
        <ul class="list">
             <li class="item-0">first item</li>
             <li class="item-1"><a href="link2.html">second item</a></li>
             <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
             <li class="item-1 active"><a href="link4.html">fourth item</a></li>
             <li class="item-0"><a href="link5.html">fifth item</a></li>
         </ul>
     </div>
 </div>
'''
from pyquery import PyQuery as pq
doc = pq(html)
li = doc('li:first-child')
print(li)
li = doc('li:last-child')
print(li)
li = doc('li:nth-child(2)')
print(li)
li = doc('li:gt(2)')
print(li)
li = doc('li:nth-child(2n+1)')
print(li)