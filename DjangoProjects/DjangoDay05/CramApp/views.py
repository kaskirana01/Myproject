import json
from datetime import timedelta

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect

# request对象，是django在客户端发起请求后，根据请求信息自动创建的
from django.views.decorators.csrf import csrf_exempt

from CramApp.models import User


# def index(request):
#
# 	# 请求方法
# 	print(request.method)
#
# 	# 请求路径
# 	print(request.path)
#
#   # 请求IP
# 	# print(request.META)
#
# 	# get请求参数
# 	print(request.GET)
# 	# post请求参数
# 	print(request.POST)
#
# 	# 文件参数
# 	print(request.FILES)
#
# 	# cookies
# 	print(request.COOKIES)
#
# 	# session
# 	print(request.session)
#
# 	return render(request,'index.html')

# 路径参数
# 127.0.0.1:8000/goods/2/
# 视图函数中第一个参数必须是request，后续即路径参数（一一对应）
# 没有参数时，num可设置默认值
def goods(request, num=1):
	temp = '第{}页 商品'.format(num)

	return HttpResponse(temp)


def sum(request, a, b, c):
	temp = 'a:{},b:{},c:{}'.format(a, b, c)
	return HttpResponse(temp)


# 参数名已经指定！?P<name>
def detail(request, name):
	temp = '{} 详情信息'.format(name)

	return HttpResponse(temp)


# get请求参数
def gettest(request):
	# QueryDict 类字典
	# 使用这种方式，如果书写的key不存在，会抛出异常。(不建议使用)
	# name = request.GET['name']
	# age = request.GET['age']

	# 通过get方法获取(没有参数返回None，推荐使用）
	name = request.GET.get('name')
	age = request.GET.get('age')
	score = request.GET.get('score')

	temp = '名字:{},年龄:{},成绩:{}'.format(name, age, score)
	return HttpResponse(temp)


# post请求参数
def postview(request):
	return render(request, 'postview.html')


@csrf_exempt  # 豁免csrf
def posttest(request):
	username = request.POST.get('username')
	temp = '用户名:{}'.format(username)
	return HttpResponse(temp)


# 重定向 (状态码）
# 2xx 成功
# 3xx 重定向
# 4xx 客户端错误
# 5xx 服务器错误
def urltest(request):
	return redirect('cramapp:goodslist', 3)  # 返回商品第三页


def jsontest(request):
	dic1 = {
		'name': '张三',
		'age': 18,
		'sex': '男'
	}
	# list1 = [1,2,3,4]
	# res = json.dumps(list1)
	# res1 = json.dumps(dic1)
	# return HttpResponse(res1)
	return JsonResponse(dic1)


# 响应方式
# HttpResponse
# render
# HttpResponseRedirect
# redirect
# JsonResponse

def index(request):
	# 通过请求request获取cookies
	username = request.COOKIES.get('username')
	return render(request, 'index.html', context={'username': username})


# 注册 cookies
def register(request):
	if request.method == 'GET':  # 获取页面
		return render(request, 'register.html')
	elif request.method == 'POST':
		# 注意1: 第一步先检查客户端是否能将用户信息 传到 服务器

		# 注意2: 获取数据的字段要保持一致
		# 获取参数
		username = request.POST.get('username')
		password = request.POST.get('password')
		tel = request.POST.get('tel')
		sex = request.POST.get('sex')
		# print(username,password,tel,sex)

		# 注意3: 检查数据已经可以存入到数据库
		# 存储到数据库中
		# 用户名唯一，如果已存在，无法保存！
		try:
			user = User()
			user.username = username
			user.password = password
			user.tel = tel
			user.sex = sex
			user.save()

			# 传递 参数 给 客户端 需要response对象
			# 要求:回到首页
			response = redirect('cramapp:index')

			# cookie方式
			# 通过响应设置cookie
			response.set_cookie('username', user.username)

			# return HttpResponse('注册成功')
			return response
		except:
			return HttpResponse('注册失败，请重新注册')


# 注销
def logout(request):
	# 注销 重定向到首页
	response = redirect('cramapp:index')

	# 删除cookies
	response.delete_cookie('username')
	return response


# 登录
def login(request):
	if request.method == 'GET':  # 获取登录页面
		return render(request, 'login.html')
	elif request.method == 'POST':  # 登录操作
		username = request.POST.get('username')
		password = request.POST.get('password')
	# print(username,password)

	# 验证  filter 是一个结果集
	users = User.objects.filter(username=username)
	# print(users)

	if users.exists():  # 用户存在  用户有唯一约束
		user = users.first()
		if user.password == password:  # 验证通过
			# 重定向 首页
			response = redirect('cramapp:index')

			# 设置cookies
			# max_age 过期时间，指定多少秒后过期
			# max_age = None 浏览器关闭失效
			# expires 过期时间, 指定过期时间
			# temp = timedelta(seconds=10)    # 当前时间加10天、minutes = 5 5分钟、

			# response.set_cookie('username',user.username,max_age=60*60*24*7)
			# 用户名为中文时，cookies会有问题
			response.set_cookie('username', user.username, max_age=60 * 60 * 24 * 1)

			return response

		else:  # 密码错误
			return render(request, 'login.html', context={'err': '用户名或密码错误！'})

	else:  # 用户不存在
		return render(request, 'login.html', context={'err': '用户名或密码错误！'})

# return HttpResponse('正在登录')
