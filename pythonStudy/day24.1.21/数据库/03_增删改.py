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
info = input('请输入学生的信息(学号,姓名,班级,用逗号隔开):')
sno,sname,sclass = info.split(',')   # 字符串拆分 元组解包
# 字符串参数 两边需要添加单引号
sql = "insert into student (sno, sname,sclass) values('{}','{}','{}') ".format(sno,sname,sclass)

# sql2 = "delete from student where sname = '{}'".format(info)   # 删
# print(sql)
# exit()     # 调试
# sql3 = "update student set sno = 1102 where sname = '{}' " .format(info)
try:
	# pymysql    自动begin开启事务,关闭了自动提交功能
	rows = cursor.execute(sql)      # 返回受影响的行数

	if rows > 0:          # 插入成功提交,失败回滚
		conn.commit()
		print('已确认')
		print(cursor.lastrowid)   # 获取最后一个主键的自增id号
	else:
		conn.rollback()

except Exception as e:
	print(e)

finally:
# 5.关闭链接
	cursor.close()
	conn.close()

