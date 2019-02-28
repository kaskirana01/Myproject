import random

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from Stu_info.models import Stu


def index(request):
	return render(request, 'index.html')


def addStu(request):
	stu = Stu()
	# print(Stu.objects.last().id)
	# tem = (Stu.objects.last().id & 1)
	# while 1:
	# 	tem += 1
	# 	break
	stu.s_name = str(random.randrange(0,100)) + '-' + '号学生'
	stu.s_sno = random.randrange(1000, 10000)
	stu.s_sex = random.choice(['男', '女'])
	stu.s_score = random.randrange(0, 100)
	stu.save()
	return HttpResponse('学生添加成功:<p>{}-姓名:{},学号:{},性别:{},分数:{}</p>'
	                    .format(stu.id, stu.s_name, stu.s_sno, stu.s_sex, stu.s_score))


def delStu(request):
	stu = Stu.objects.last()
	stu.delete()
	return HttpResponse('删除学生成功')


def showallStu(request):
	stus = Stu.objects.all()

	response_str = '<h3>查询的所有学生为:</h3>'
	for stu in stus:
		response_str += '<p>{}-姓名:{},学号:{},性别:{},分数:{}</p>' \
			.format(stu.id, stu.s_name, stu.s_sno, stu.s_sex, stu.s_score)
	return HttpResponse(response_str)


def delall(request):
	stu = Stu.objects.all()
	stu.delete()
	return HttpResponse('删除所有学生成功')
