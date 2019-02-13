# 自定义app应用
from templates import *
from views import *
from urls import *
from myRequest import *
import re
def application(environ,start_response):
	# print(environ)
	# 遍历environ字典
	# for key in environ:
	# 	print(key,'----',environ[key])
	html = "<!doctype html><html><head><meta charset='utf-8'></head><body><h2>你好</h2></body></html>"

	# 处理路由，将用户的请求转化为对应的处理
	path = environ.get('PATH_INFO','/')    # 字典的get方法，不会报错
	path = path.strip('/')      # 去掉前后'/'匹配
	print(path)

	# 生成请求对象
	request = MyRequest(environ,start_response)

	# 第一版路由
	# if path == '/':
	# 	return index(environ,start_response)
	# elif path == '/login':   # 登陆界面
	# 	return login(environ,start_response)

	# 第二版路由
	for url,func in urlpatterns:    # url 为匹配规则，func为函数
		print(url,func)
		if re.match(url,path,re.I):
			return func(request)

	start_response('200 ok',[('Content-Type','text/html')])    # （响应头）

	return [html.encode('utf-8')]    # 字节流（b）交流（响应体）