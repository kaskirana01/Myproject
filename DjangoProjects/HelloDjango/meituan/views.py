import random
from django.http import HttpResponse
from django.shortcuts import render

# 视图函数 第一个参数必须是request
from .models import Student

from .models import User


def index(request):
	return HttpResponse('美团')


def home(request):
	return HttpResponse('home页')


# 返回模板
def cart(request):
	return render(request, 'cart.html')


def addstu(request):
	stu = Student()
	stu.name = '张三' + str(random.randrange(1, 1000000))
	stu.score = random.randrange(1, 100)

	# 存到数据库中
	stu.save()

	return HttpResponse('增加学生' + stu.name)


def addUser(request):
	user = User()
	user.username = '李四' + str(random.randrange(1, 1000000))
	user.password = random.randrange(1, 100)

	user.save()
	return HttpResponse('增加用户' + user.username)
