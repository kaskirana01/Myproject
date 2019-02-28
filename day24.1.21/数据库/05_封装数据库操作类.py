# from _sha1 import sha1

import pymysql
from settings import database
from hashlib import sha1

"""
SELECT {fields} FROM {table}{where}{groupby}{having}{orderby}{limit}.format()
"""
class Manager:
	def __init__(self,tableName):
		self.tableName = tableName    # 数据库表名

		self.conn = self.__connect(**database)   # 连接数据库,传入键值对字符串,参数见配置文件settings

		self.cursor = self.conn.cursor(cursor=pymysql.cursors.DictCursor)   # 游标

		self.options = self.__initOptions()   # 初始化查询参数字典

	def __del__(self):      # 析构函数关闭对象和链接
		self.cursor.close()
		self.conn.close()

	def __connect(self,**kwargs):
		"""
		自定义的链接数据库方法
		:param kwargs:  数据库链接参数字典
		:return:   连接对象
		"""
		return pymysql.Connect(**kwargs)

	def __initOptions(self,**kwargs):
		"""
		初始化查询参数字典
		:param kwargs: 字典,保存查询参数
		:return:
		"""
		return {
			'fields':'*',
			'table':self.tableName,
			'where':"",
			'groupby':"",
			'having':"",
			'orderby':"",
			'limit':"",
			'values':""
		}

	def where(self,**kwargs):
		"""
		传入的值可能是{'user':'root','password':'123'}
		要变成 where user = 'root' and password ='123'
		:param kwargs:   键值对
		:return:
		"""
		if len(kwargs)== 0:   # 如果为空字典,直接返回对象
			return self
		if not self.options["where"]:  # 判断字典中where键值是不是为空
			self.options['where'] = " where "   # 如果为空 则添加where
		else:
			self.options['where'] += ' and '    # 如果有where 则拼接and
		ops = {
			'gt': '>',
			'gte': '>=',
			'lt': '<',
			'lte': '<=',
			'ne': '<>'
		}
		# 拼接参数
		for key in kwargs:
			op = key.split("__")  # 得到键和运算符
			if isinstance(kwargs[key], str):
				if len(op) > 1:
					self.options['where'] += op[0] + ops[op[1]] + "'" + pymysql.escape_string(
						kwargs[key]) + "'" + ' and '              # 加引号
				else:
					self.options['where'] += op[0] + "=" + "'" + pymysql.escape_string(kwargs[key]) + "'" + ' and '
			# self.options['where'] += key + " = '" + pymysql.escape_string(kwargs[key]) + "'" + ' and '
			else:
				if len(op) > 1:
					self.options['where'] += op[0] + ops[op[1]] + str(kwargs[key]) + ' and '
				else:
					self.options['where'] += op[0] + "=" + str(kwargs[key]) + ' and '

			# self.options['where'] += key + " = " + str(kwargs[key]) + ' and '
		self.options['where'] = self.options['where'].rstrip('and ')  # 去除最后的and

		return self

	def orderby(self,*args):
		if len(args) <= 0:
			return self
		if not self.options['orderby']:
			self.options['orderby'] = ' order by '
		else:
			self.options['orderby'] += ' , '
		# 生成一个字段列表
		self.options['orderby'] += ','.join(args)
		return self

	def groupby(self,*args):
		pass

	def having(self,*args):
		pass

	def values(self,*args):       # 生成字段列表
		if len(args) <= 0:
			return self
		self.options['fields'] = ','.join(args)
		return self

	def select(self):
		sql = "SELECT {fields} FROM {table}{where}{groupby}{having}{orderby}{limit}".format(**self.options)

		return self.query(sql)   #  调用query方法查询

	def addQuote(self,data):     # 修改字典，不需要返回值
		for key in data:
			if isinstance(data[key],str):
				data[key] = "'" + data[key] + "'"       # 给value加引号，不能直接修改value的值

	def getKeyValuesList(self,data):
		"""
		获取键列表和值列表
		:param data:  参数字典
		:return:
		"""
		keys = ''
		values = ''
		for key in data:
			keys += key + ','
			values += str(data[key]) + ','
		return keys.rstrip(','),values.rstrip(',')

	def insert(self,data):
		"""
		字典
		:param data: 字典， { 'sno':'009','sname':'tom'}
		:return: 成功返回True，失败返回False
		"""
		# 1.如果值是字符串，要添加单引号
		self.addQuote(data)

		# 2.拆分字典，生成键的列表fields，值的列表values，替换
		keys,values = self.getKeyValuesList(data)
		self.options['fields'] = keys
		self.options['values'] = values

		# 3.执行
		sql = "INSERT INTO {table}({fields}) VALUES ({values})".format(**self.options)
		return self.excute(sql)
		# print(sql)     # INSERT INTO student(sno,sname,sage) VALUES ('009','tom',20)

	def excute(self,sql):
		"""
		执行增删改
		:param sql:
		:return: 成功返回True，失败返回False
		"""
		if not sql:
			return False
		self.options = self.__initOptions()
		self.sql = sql
		try:
			rows = self.cursor.execute(sql)
			if rows >0:
				self.conn.commit()
				return True
			else:
				self.conn.rollback()
				return False
		except Exception as e:
			print(e)
			self.conn.rollback()
			return False

	def delete(self):
		sql = "DELETE FROM {table}{where}".format(**self.options)
		return self.excute(sql)

	def update(self,data):
		"""
		更新记录
		:param data: 字典
		:return:
		"""
		self.addQuote(data)         # values 需要处理，：变为= ，这里先加引号
		self.options['values'] = ','.join([key + "=" + str(value) for key,value in data.items()])
		sql = "UPDATE {table} SET {values}{where}".format(**self.options)
		return self.excute(sql)

	def query(self,sql):   # (将查询方法单独列出来，可以使用原生sql语句查询）
		if not sql:
			return None
		self.sql = sql     # 保存sql
		self.options = self.__initOptions()      # 参数字典初始化
		try:
			rows = self.cursor.execute(sql)      # 执行sql语句
			if rows > 0 :
				return self.cursor.fetchall()
			else:
				return None
		except Exception as e:
			print(e)
			return None

	def limit(self,*args):
		"""
		(10,20)
		:param args:   limit 只能有两个参数 从第几行开始选多少行
		:return:
		"""
		self.options['limit'] += ' limit '
		for value in args:
			self.options['limit'] += str(value) + ' , '
		self.options['limit'] = self.options['limit'].rstrip(', ')
		return self

if  __name__ == "__main__":
	db = Manager('student')    # user
	# sql = "SELECT {fields} FROM {t able}{where}{groupby}{having}{orderby}{limit}".format(**self.options)

	# print(db.options)
	# print(sql)
	# db.where(name = 'yi',password = sha1('1129'.encode('utf-8')).hexdigest()).limit(0,1).select()
	# db.where(name = 'admin').select()   # 查询后需要初始化字典
	# data1 = db.where(sname = '李军').select()
	# data2 = db.query("select * from student")
	# print(data1,'\n',data2)
	# data1 = db.values('sno','sname').where(sclass='95031').orderby('sno desc','sname').select()
	# print(db.sql)
	# print(data1)
	# flag = db.insert({'sno':'009','sname':'tom','sclass':95031})
	# print(flag)
	# flag = db.where(sno='009').delete()
	# print(flag)
	# flag = db.update({'sbirthday':'2009-3-13'})    # 记得加where
	# print(flag)
	data = db.where(sno__gt='003').select()
	print(data)

	"""
	all()  获取所有记录
	get  根据主键获取一条记录
	getByxxx  xxx sname 
	"""