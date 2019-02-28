import pymysql

# 1.链接数据库
# 参数： 服务器地址，用户名，密码，数据库名，端口（默认3306），指定字符集。
conn = pymysql.connections.Connection(host='localhost',
                                      user='root',
                                      password=' ',
                                      database='practice',
                                      port=3306,
                                      charset='utf8'
                                      )

# 2.创建一个游标对象。
# 如果不指定参数，默认返回元组:(('101', '李军', '男'), ('103', '陆君', '男'), ('105', '匡明', '男'), ('107', '王丽', '女'), ('108', '曾华', '男'))
cursor  = conn.cursor(cursor=pymysql.cursors.DictCursor)
# 如果指定参数， 返回是列表：
# [{'sno': '101', 'sname': '李军', 'ssex': '男'}, {'sno': '103', 'sname': '陆君', 'ssex': '男'}, {'sno': '105', 'sname': '匡明', 'ssex': '男'}, {'sno': '107', 'sname': '王丽', 'ssex': '女'}, {'sno': '108', 'sname': '曾华', 'ssex': '男'}]

# 3.执行sql语句.
sno = input('请输入学生的姓名:')

# 字符串参数 两边需要添加单引号
sql = "select sno,sname,ssex from student where sname like '{}%'".format(sno)
# print(sql)

try:
	rows = cursor.execute(sql)    # 返回受影响的行数

	if rows > 0:
		# print(rows)   6
		# 4.读取结果集
		# data = cursor.fetchone()   # 获取一条记录
		# data = cursor.fetchmany(5)  # 获取n=5条记录
		data = cursor.fetchall()  # 获取所有记录
		print(data)
		# print(cursor._executed)  # 获取所执行的sql语句
except Exception as e:
	print(e)


finally:
# 5.关闭链接
	cursor.close()
	conn.close()

