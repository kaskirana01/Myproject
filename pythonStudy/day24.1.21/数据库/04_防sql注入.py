import pymysql
from hashlib import sha1

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
name = input('请输入用户名:')
password = input('请输入密码:')
password = sha1(password.encode('utf-8')).hexdigest()
print(password)
# exit()

# 字符串参数 两边需要添加单引号
# sql = "select id from user where name ='{}' and password = '{}'".format(name,password)
# print(sql)

# 注入式攻击!!!!!
# 请输入用户名:lll ' or ' 1 ' or '
# 请输入密码:asdakldjal
# 0f943058f14c994eefe0525b2b17bc4f5f701637
# 登陆成功

# 防止注入式攻击的两种方法
# 1.使用escape方法转义字符串中的特殊字符(','等)
# name = pymysql.escape_string(name)
# sql = "select id from user where name = '{}' and password = '{}'".format(name,password)

# 2.使用execute方法本身的转义功能,参数传给rows.
sql = "select id from user where name = %s and password = %s"


# print(name)           # lll \' or \'1 \' or
# exit()    测试  养成这个小习惯!

try:
	rows = cursor.execute(sql,(name,password))   # 返回受影响的行数
	print(cursor._executed)    # select id from user where name = 'lll \' or \'1 \'or \'' and password = '40bd001563085fc35165329ea1ff5c5ecbdbbeef'

	if rows > 0:
		# print(rows)   6

		print("登陆成功")
	else:
		print("登录失败")
except Exception as e:
	print(e)

finally:
# 5.关闭链接
	cursor.close()
	conn.close()

