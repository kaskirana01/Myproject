# 定义各种处理
from _sha1 import sha1
from urllib.parse import parse_qs  # 字符串处理库
from Manager import Manager
import jinja2



# 首页
# def index(envirn,start_response):
# 	try:
# 		with open('templates/网站作业2.html') as fp:
# 			data = fp.read()
# 		start_response('200 ok', [('Content_Type', 'text/html')])
# 		return [data.encode('utf-8')]
# 	except Exception as e:
# 		data = 'File Not Found'
# 		start_response('404 Not Found',[('Content_Type', 'text/html')])
# 		return [data.encode('utf-8')]

# 首页第二版写法
def index(request):
	request.start_response('200 ok', [('Content-Type', 'text/html')])
	return [
		"<!doctype html><head><meta charset='utf-8'><meta http-equiv='refresh' content='3;url=http://localhost:8090/login'></head><body><h1>您好：欢迎访问！</h1><h4>3秒钟后跳转到登录页面！</h4></body></html>".encode(
			'utf-8')]


# 登录界面
# def login(envirn,start_response):
# 	try:
# 		with open('templates/login.html') as fp:
# 			data = fp.read()
# 		start_response('200 ok', [('Content_Type', 'text/html')])
# 		return [data.encode('utf-8')]
# 	except Exception as e:
# 		data = 'File Not Found'
# 		start_response('404 Not Found',[('Content_Type', 'text/html')])
# 		return [data.encode('utf-8')]

# 封装请求参数后第二版登录
def login(request):
	try:
		with open('templates/login.html') as fp:
			data = fp.read()
		request.start_response('200 ok', [('Content-Type', 'text/html')])
		return [data.encode('utf-8')]
	except Exception as e:
		data = 'File Not Found'
		request.start_response('404 Not Found', [('Content-Type', 'text/html')])
		return [data.encode('utf-8')]


# 登录处理(第一版）
# def doLogin(envirn,start_response):
# 	print(envirn.get('QUERY_STRING'))
# 	# 把参数字符串转化成字典
# 	paras = parse_qs(envirn.get('QUERY_STRING',''))
#
# 	# 获取用户名密码
# 	username = paras.get('username')
# 	if username :
# 		username = username[0]
# 	password = paras.get('password')
# 	if password:
# 		password = password[0]
# 		#sha转换
# 		password = sha1(password.encode('utf8')).hexdigest()
# 	print(username,password)
#
# 	# 数据库操作
# 	db = Manager('student')
# 	result = db.where(sname=username,password=password).select()
# 	print(result)
# 	start_response('200 ok', [('Content_Type', 'text/html')])
#
# 	# 如果查询成功
# 	if result:
# 		html=""
# 		with open('templates/tip.html') as fp:
# 			html = fp.read()
# 		return [html.encode('utf-8')]
# 	else:
# 		return ["用户名或密码错误，请重新登录".encode('utf-8')]

def doLogin(request):
	# 把参数字符串转化为字典
	paras = request.GET
	print(paras)
	username = paras.get('username')
	password = paras.get('password')
	print(username,password)

	password = sha1(password.encode('utf8')).hexdigest()  #如果签名，需要转换
	print(username,password)

	# 数据库操作
	db = Manager('student')
	result = db.where(sname=username, password=password).select()
	request.start_response('200 ok', [('Content-Type', 'text/html')])

	# 如果查询成功
	if result:
		html = ""
		with open('templates/tip.html') as fp:
			html = fp.read()
		return [html.encode('utf-8')]
	else:
		html = ""
		with open('templates/tip2.html') as fp:
			html = fp.read()
		return [html.encode('utf-8')]


def studentList(request):
	db = Manager('student')
	data = db.values('sname,password,snum').select()
	print(data)
	env = jinja2.Environment(loader=jinja2.FileSystemLoader('./templates'))
	template = env.get_template('studentlist.html')
	print(template)
	request.start_response('200 ok', [('Content-Type', 'text/html')])
	return [template.render(students=data).encode('utf-8')]

def register(request):
	html = b''
	with open('templates/register.html','rb') as fp:
		html = fp.read()
	request.start_response('200 ok', [('Content-Type', 'text/html')])
	return [html]

def loadStatic(request):
	path = request.path.strip('/')
	# print(path)
	import os
	ext = os.path.splitext(path)[1].strip('.')
	print(ext)
	if os.path.exists(path):
		with open(path,'rb') as fp:
			content = fp.read()
		if ext == 'css':
			request.start_response('200 ok', [('Content-Type', 'text/css')])
		elif ext == 'js':
			request.start_response('200 ok', [('Content-Type', 'application/x-javascript')])
		elif ext == 'png':
			request.start_response('200 ok', [('Content-Type', 'image/png')])
		elif ext in ['jpeg','jpg']:
			request.start_response('200 ok', [('Content-Type', 'image/jpeg')])
	else:
		content = b"file not found"
		request.start_response('200 ok', [('Content-Type', 'text/html')])

	return [content]

def yzm(request):
	from VerifyCode import VerifyCode
	vc = VerifyCode()
	data = vc.generate()
	request.start_response('200 ok', [('Content-Type', 'image/png')])
	return [data]

# 学生信息
def studentInfo(request,sno):
	print(sno)
	request.start_response('200 ok', [('Content-Type', 'text/html')])
	return [b'info']
