# 封装请求类
from urllib.parse import parse_qs

class MyRequest:
	def __init__(self,environ,start_response):
		self.start_response = start_response
		self.environ = environ

		# 请求方法
		self.method = environ.get('REQUEST_METHOD','GET')   # 没有的话默认get
		# 请求路径
		self.path = environ.get('PATH_INFO','/')    # 没有的话默认首页/
		# get参数
		self.GET = self.get_paramrters()

	# 获取get参数
	def get_paramrters(self):
		queryString = self.environ.get('QUERY_STRING','')   # 得到查询字符串，默认为空
		# print("queryString",queryString)
		data = parse_qs(queryString)    # 这是一个字典 {'username':['admin']}
		# print('data',data)
		for key in data:
			if len(data[key]) ==1 :
				data[key] = data[key][0]      # 如果字典中键所对应的值只有一个值，则去掉值的列表，保留那一个值
		return data

