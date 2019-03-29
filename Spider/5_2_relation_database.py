#!/usr/bin/python

import pymysql

db = pymysql.connect(host='localhost',user='root',password='1qaz#EDC',port=3306, db='spiders')

cursor = db.cursor()

cursor.execute('SELECT VERSION()')

data = cursor.fetchone()

print('Database version:',data)

#cursor.execute('CREATE DATABASE spiders DEFAULT CHARACTER SET utf8')

sql = 'CREATE TABLE IF NOT EXISTS students \
        (id VARCHAR(255) NOT NULL, name VARCHAR(255) NOT NULL, age INT NOT NULL, PRIMARY KEY (id))'
#cursor.execute(sql)

id = '20120002'
user = 'Bob'
age = 20
 
sql = 'INSERT INTO students(id, name, age) values(%s, %s, %s)'
try:
    cursor.execute(sql, (id, user, age))
    db.commit()
except:
    print('Failed')
    db.rollback()


data = {
    'id': '20120003',
    'name': 'Bob',
    'age': 20
}
table = 'students'
keys = ', '.join(data.keys())
values = ', '.join(['%s'] * len(data))
print(values)
print(tuple(data.values()))
sql = 'INSERT INTO {table}({keys}) VALUES ({values})'.format(table=table, keys=keys, values=values)
print(sql)
try:
   if cursor.execute(sql, tuple(data.values())):
       print('Successful')
       db.commit()
except:
    print('Failed')
    db.rollback()

sql = 'UPDATE students SET age = %s WHERE name = %s'
try:
   cursor.execute(sql, (25, 'Bob'))
   db.commit()
except:
   db.rollback()

data = {
    'id': '20120004',
    'name': 'Bob',
    'age': 21
}
 
table = 'students'
keys = ', '.join(data.keys())
values = ', '.join(['%s'] * len(data))
 
sql = 'INSERT INTO {table}({keys}) VALUES ({values}) ON DUPLICATE KEY UPDATE'.format(table=table, keys=keys, values=values)
update = ','.join([" {key} = %s".format(key=key) for key in data])
sql += update
print('sql is ' + sql)
try:
    if cursor.execute(sql, tuple(data.values())*2):
        print('Successful')
        db.commit()
except:
    print('Failed')
    db.rollback()


sql = 'SELECT * FROM students WHERE age >= 20'
 
try:
    cursor.execute(sql)
    print('Count:', cursor.rowcount)
    one = cursor.fetchone()
    print('One:', one)
    results = cursor.fetchall()
    print('Results:', results)
    print('Results Type:', type(results))
    for row in results:
        print(row)
except:
    print('Error')

db.close()

