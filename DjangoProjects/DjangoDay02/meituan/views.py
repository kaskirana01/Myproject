import random

from django.db.models import Max, Avg, Q, F
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from meituan.models import student


def index(request):
	return HttpResponse('欢迎来到美团！')


def addStu(request):
	stu = student()
	# stu.s_id =
	stu.s_name = str(random.randrange(1, 100)) + 'yi-'
	stu.s_score = random.random() * 100
	stu.s_math = random.random() * 100
	stu.s_english = random.random() * 100
	stu.s_weight = random.randrange(1, 100)
	stu.s_height = random.randrange(1, 100)
	stu.s_detil = '我爱python'
	stu.s_delete = True
	# stu.s_create = ''
	# stu.s_change = ''
	stu.save()

	return HttpResponse('添加学生成功' + stu.s_name)


def changestu(request):
	return HttpResponse('更新学生信息')


# 结果集合[]
def showstudents(request):
	# 获取所有学生信息
	# all() 所有数据
	students = student.objects.all()

	# filter() 符合条件的数据
	# id == 3的
	# students = student.objects.filter(s_id=3)
	# id < 3的
	# students = student.objects.filter(s_id__lt=3)
	# score >= 60
	# students = student.objects.filter(s_score__gte=60)
	# id>3 且 成绩<60
	# students = student.objects.filter(s_id__gt=3).filter(s_score__lt=60)
	# students = student.objects.filter(s_id__gt=3,s_score__lt=60)

	# exclude()  过滤符合要求的
	# 不显示id为3的
	# students = student.objects.exclude(s_id=3)

	# 模糊查询
	# 名字以7开头的
	# students = student.objects.filter(s_name__startswith='7')
	# 名字以#结尾的
	# students = student.objects.filter(s_name__endswith='#')
	# 名字带有8的
	# students = student.objects.filter(s_name__contains=8)

	# 排序
	# 按成绩排序 默认升序，加'-'降序
	# students = student.objects.order_by('s_score')  # 升序
	# students = student.objects.order_by('-s_score')  # 降序

	# in
	# 找id为1，2，3，7，9
	# students = student.objects.filter(s_id__in=[1,2,3,7,9])

	# 切片
	# students = student.objects.order_by('-s_score')[0:3]

	# 显示学生信息
	student_str = ''
	for stu in students:
		student_str += '<p>{}-姓名:{},成绩:{},体重:{},身高:{},数学:{},英语:{}</p>'.format(
			stu.s_id, stu.s_name, stu.s_score, stu.s_weight,stu.s_height,stu.s_math,stu.s_english)

	return HttpResponse(student_str)

# 获取单个数据，非结果集
def showstu(request):
	# get() 符合要求的
	# id == 3
	# stu = student.objects.get(s_id=3)
	# pk 是primary key的缩写
	# stu = student.objects.get(pk=3)

	# 当数值重复时，get会报错
	# stu = student.objects.get(s_score=99)   如果有两个99，则会异常
	# 如果数据不存在，也会抛出异常'DoesNotExist'
	# stu = student.objects.get(pk=100)

	# first() 获取第一个数据
	# stu = student.objects.first()
	# stu = student.objects.filter(s_score=99).first()

	# last() 获取最有一个数据
	# stu = student.objects.filter(s_score=99).last()

	# count() 个数
	students = student.objects.filter(s_score__gt=90)
	stu_str = ''
	if students.count():
		for stu in students:
			stu_str += '<p>{}-姓名:{},成绩:{},体重:{},身高:{},数学:{},英语:{}</p>'.format(stu.s_id,
			stu.s_name, stu.s_score, stu.s_weight,stu.s_height,stu.s_math,stu.s_english)
		return HttpResponse(stu_str)
	else:
		return HttpResponse('该学员不存在')

	# return HttpResponse(stu_str)
def agg(request):

	# Max()、Min()、Avg()... 需要导包,必须放到aggregate()函数里面
	# 求最大值
	# maxDir = student.objects.aggregate(Max('s_score')) # {'s_score__max': 99}
	# print(maxDir['s_score__max'])   # 99
	# #最高分的学生信息可能不止一个
	# students = student.objects.filter(s_score = maxDir['s_score__max'])
	#
	# student_str = ''
	# for stu in students:
	# 	student_str += '<p>{}-姓名:{},成绩:{},体重:{},身高:{} </p>'.format(
	# 		stu.s_id, stu.s_name, stu.s_score, stu.s_weight,stu.s_height)
	#
	# return HttpResponse(student_str)

	# id为[1,2,3]的平均成绩
	avgDir = student.objects.filter(s_id__in=[1,2,3]).aggregate(Avg('s_score'))
	print(avgDir)

	return HttpResponse('id为1，2，3的学生平均分为:' + str(avgDir['s_score__avg']))

# Q对象 （将条件进行封装,可用于不同属性的对比）
def Qtest(request):
	# 条件封装
	# & 与
	# | 或
	# ～ 非

	# 或   id 大于15 或 成绩小于30
	# Q(s_id__gt=15）
	# Q(s_score__lt=30)
	# students = student.objects.filter(Q(s_id__gt=15) | Q(s_score__lt=30))

	# 且   id>3 且 成绩<60
	# Q(s_id__gt=3)
	# Q(s_score__lt=60)
	# students = student.objects.filter(Q(s_id__gt=3) & Q(s_score__lt=60))

	# 取反   不显示id为3的
	# Q(s_id=3)
	# ~Q(s_id=3)
	students = student.objects.filter(~Q(s_id=3))

	student_str = ''
	for stu in students:
		student_str += '<p>{}-姓名:{},成绩:{},体重:{},身高:{},数学:{},英语:{} </p>'.format(
			stu.s_id, stu.s_name, stu.s_score, stu.s_weight,stu.s_height, stu.s_math, stu.s_english)

	return HttpResponse(student_str)

# F对象 （自己和自己比较）
def Ftest(request):
	# F对象， 实现自己和自己比较
	# 英语成绩 大于 数学成绩的 学生信息
	students = student.objects.filter(s_english__gt=F('s_math'))
	student_str = ''
	for stu in students:
		student_str += '<p>{}-姓名:{},成绩:{},体重:{},身高:{},数学:{},英语:{} </p>'.format(
			stu.s_id, stu.s_name, stu.s_score, stu.s_weight, stu.s_height, stu.s_math, stu.s_english)

	return HttpResponse(student_str)
