# from _sha1 import sha1

import pymysql
from settings import database
from hashlib import sha1

"""
SELECT {fields} FROM {table}{where}{groupby}{having}{orderby}{limit}
"""
class Manager:
	def __init__(self,tableName):
		self.tableName = tableName    # 数据库表名

		self.conn = self.__connect(**database)   # 连接数据库,传入键值对字符串,参数见配置文件settings

		self.cursor = self.conn.cursor(cursor=pymysql.cursors.DictCursor)   # 游标

		self.options = self.__initOptions()   # 初始化查询参数

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
			'limit':""
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
		if not self.options["where"]:  # 判断字典中没有where键
			self.options['where'] = " where "   # 如果没有where 则添加
		else:
			self.options['where'] += ' and '    # 如果有where 则拼接

		for key in kwargs:   # 遍历字典,用 = 替换 : ,and 链接多个键值对
			if isinstance(kwargs[key],str):
				self.options['where'] += key + " = '" + kwargs[key] +"'" + ' and '  # 如果是字符串,加引号 and后有空格
			else:
				self.options['where'] += key + " = " + str(kwargs[key]) + ' and '  # and后有空格

		self.options['where'] = self.options['where'].rstrip('and ')   # 右截最后的and空格
		# print(self.options)
		return self

	def select(self):
		sql = "SELECT {fields} FROM {table}{where}{groupby}{having}{orderby}{limit}".format(**self.options)
		try:
			rows = self.cursor.execute(sql)
			if rows > 0:
				data = self.cursor.fetchall()
				print(data)

		except Exception as e:
			print(e)
		print(sql)
		# return sql

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
	db = Manager('user')
	# sql = "SELECT {fields} FROM {t able}{where}{groupby}{having}{orderby}{limit}".format(**self.options)

	# print(db.options)
	# print(sql)
	db.where(name = 'yi',password = sha1('1129'.encode('utf-8')).hexdigest()).limit(0,1).select()