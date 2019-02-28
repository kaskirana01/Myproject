import pymysql
from settings import database

class Manager:
	def __init__(self,tableName):
		self.tableName = tableName
		self.conn = self.__connect(**database)
		self.cursor = self.conn.cursor(cursor=pymysql.cursor.DictCursor)
		self.options = self.__initOptions()

	def __del__(self):
		self.cursor.close()
		self.conn.close()

	def __connect(self,**kwargs):
		return pymysql.Connect(**kwargs)


	def __initOptions(self,**kwargs):
		return {
			'fields':'*',
			'table':self.tableName,
			'groupby':"",
			'having':"",
			'orderby':"",
			'limit':"",
			'values':""
		}

	def where(self,**kwargs):
		if len(kwargs)== 0:
			return self
		if not self.options['where']:
			self.options['where'] = ' where '
		else:
			self.options['where'] += ' and '
