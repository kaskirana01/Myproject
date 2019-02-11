from pymongo import MongoClient

# 链接mongo
conn = MongoClient(host='localhost')
# print(conn)

# 链接数据库
db = conn.student
# print(db)

# 查询
# data = db.student.find()
# # print(data)   返回一个可迭代对象
# data1 = db.student.find({'name':"yi"})
# for value in data:
# 	print(value)
# print(next(data1))

# 插入
db.student.insert({'name':'tom','age':20})
data2 = db.student.find()
print(list(data2))

conn.close()