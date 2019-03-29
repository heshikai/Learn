#!/usr/bin/python

import pymongo
#
client = pymongo.MongoClient(host='localhost',port=27017)
db = client.tutorial
results = db.QuoteItem.find()
print(results)
for result in results:
    print(result)
#
#db = client.test
#
#collection = db.students
#
#student1 = {
#    'id':'1637',
#    'name':'Jordan',
#    'age':20,
#    'gender':'male'
#}
#
#student2 = {
#    'id':'1638',
#    'name':'Kevin',
#    'age':22,
#    'gender':'male'
#}
#
#result = collection.insert_many([student1,student2])
#print(result)
#
#result = collection.find_one({'name':'Mike'})
#
#print(result)
#
#results = collection.find({'name':'Mike'})
#for result in results:
#    print(result)
#
#
#results = collection.find({'name':'Jordan'})
#for result in results:
#    print(result)
#
#results = collection.find({'age':{'$gt':20}})
#for result in results:
#    print(result)
#
#results = collection.find({'age':{'$regex':'^M.*'}})
#for result in results:
#    print(result)
#
#count = collection.find().count()
#print(count)
#
#results = collection.find().sort('name',pymongo.ASCENDING)
#for result in results:
#    print(result['name'])
#
#results = collection.find()
#for result in results:
#    print(result['name'])
#
#results = collection.find().sort('name',pymongo.ASCENDING).skip(2).limit(2)
#
#print([result['name'] for result in results])
#
#condition = {'name':"Kevin"}
#
#student = collection.find_one(condition)
#student['age'] = 25
#
#result = collection.update(condition,student)
#print(result)
#
#condition = {'age':{'$gt':20}}
#result = collection.update_one(condition,{'$inc':{'age':1}})
#print(result)
#print(result.matched_count,result.modified_count)
#
#condition = {'age':{'$gt':10}}
#result = collection.update_many(condition,{'$inc':{'age':1}})
#print(result)
#print(result.matched_count,result.modified_count)
#


#from redis import StrictRedis as sr

#redis = sr(host = 'localhost',port=6379,db=0,password='foobared')

#redis.set('name','Bob')
#print(redis.get('name'))



