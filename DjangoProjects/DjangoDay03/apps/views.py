import random

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from apps.models import Animal, Person, IDCard, Grade, Student, User, Goods


def index(request):
	return render(request,'index.html')


def animal(request):
	return render(request,'animal.html')


def addanimal(request):
	animal = Animal()
	animal.name = str(random.randrange(1,100))+ '阿猫阿狗'
	animal.age = random.randrange(1,10)
	animal.save()
	return HttpResponse('添加数据成功')


def selectanimal(request):
	# animals = Animal.objects.all()
	# 逻辑删除的要去除掉
	# animals = Animal.objects.exclude(is_del=True)

	animals = Animal.myObjects.all()

	animal_str = ''
	for item in animals:
		animal_str += '<p>{}-{}-{}</p>'.format(item.id,item.name,item.age)

	return HttpResponse(animal_str)


def deleteanimal(request):
	animal = Animal.myObjects.last()
	animal.delete()
	return HttpResponse('删除数据成功')


def updateanimal(request):
	animal = Animal.myObjects.last()
	animal.name = '大马猴'
	animal.save()

	return HttpResponse('数据更新成功')

##################################
# 一对一
def onetoone(request):
	return render(request,'onetoone.html')

def addperson(request):
	person = Person()
	person.p_name = 'Atiom-' + str(random.randrange(1,100))
	person.save()

	return render(request,'addperson.html')


def bindcard(request):
	card = IDCard()
	card.i_no = '420923{}{}{}{}'.format(random.randrange(
		1900,2020),random.randrange(1,13),random.randrange(1,30),random.randrange(1000,10000))

	card.i_sex = random.randrange(1,3)
	card.i_addr = '大学城创客小镇16#3楼 Python1812 座位号:' + str(random.randrange(1,70))

	# 谁的身份证(绑定在最后一个人身上）。
	# 选中一个人，直接赋值一个对象
	person = Person.objects.last()
	card.i_person = person

	card.save()

	return HttpResponse('身份证绑定成功')


def deleteperson(request):
	person = Person.objects.last()
	person.delete()
	return HttpResponse('删除人成功')


def deleteIDcards(request):
	card = IDCard.objects.last()
	card.delete()
	return HttpResponse('身份证删除成功')

# 获取人对应的身份证
def getperson_card(request):
	person = Person.objects.last()

	# 主表 获取 从表信息(模型类没有对应属性，隐形访问,模型类小写)
	card = person.idcard  # 模型类IDCard小写

	if card.i_sex == 1:
		temp = '男'
	else:
		temp = '女'
	response_str = '姓名:{},性别:{},身份证号:{},家庭住址:{}'\
		.format(person.p_name,temp,card.i_no,card.i_addr)

	return HttpResponse(response_str)

# 获取身份证对应的人
def getcard_person(request):
	card = IDCard.objects.last()

	# 从表 获取 主表信息(模型类有对应的属性，显示访问)
	person = card.i_person

	if card.i_sex == 1:
		temp = '男'
	else:
		temp = '女'
	response_str = '姓名:{},性别:{},身份证号:{},家庭住址:{}'\
		.format(person.p_name,temp,card.i_no,card.i_addr)

	return HttpResponse(response_str)

######################################
# 一对多
def onetomany(request):
	return render(request, 'onetomany.html')

def addgrade(request):
	grade = Grade()
	arr = ['Python','ios','UI','Android']
	temp = random.randrange(0,len(arr))
	grade.g_name = arr[temp] + '19' + str(random.randrange(10,100))

	grade.save()
	return render(request,'addgrade.html')

def addstudent(request):
	stu = Student()
	arr = ['张三','李四','王五','赵柳','田七']
	temp = random.randrange(0,len(arr))
	stu.s_name = arr[temp] + '-' + str(random.randrange(10,100))
	stu.s_age = random.randrange(18,38)

	# 班级
	grade = Grade.objects.last()
	stu.s_grade = grade

	stu.save()
	return HttpResponse('添加学生成功')

def delgrade(request):
	grade = Grade.objects.last()
	grade.delete()

	return HttpResponse('删除班级成功')


def delstudent(request):
	stu = Student.objects.last()
	stu.delete()
	return HttpResponse('删除学生成功')

# 获取班级对应的学生
def getgrade_stu(request):
	grade = Grade.objects.last()

	# 主表获取从表信息（隐式访问）
	# 书写方式 : 模型类小写_set  类似于objects
	students = grade.student_set.all()    # 一对多（集合）

	students_str = '<h3>{}(班级人数:{})</h3>'.format(grade.g_name,students.count())
	for stu in students:
		students_str += '<p>{}-学生姓名:{}，年龄:{}</p>'.format(
			stu.id,stu.s_name,stu.s_age
		)
	return HttpResponse(students_str)

# 获取学生对应的班级
def getstu_grade(request):
	students = Student.objects.all()

	students_str = ''
	for stu in students:
		# 获取 学生 对应 班级
		# 从表 获取 主表，存在s_grade属性 显示访问
		grade = stu.s_grade

		if grade:
			students_str += '<p>{}-学生姓名:{}，年龄:{} 【{}】</p>'.format(
			stu.id, stu.s_name, stu.s_age,grade.g_name
		)
		else:
			students_str += '<p>{}-学生姓名:{}，年龄:{} 【无班级信息】</p>'.format(
				stu.id, stu.s_name, stu.s_age
			)
	return HttpResponse(students_str)

###################################
# 多对多
def manytomany(request):
	return render(request,'manytomany.html')


def adduser(request):
	user = User()
	arr = ['张三','李四','王五','赵柳','田七']
	temp = random.randrange(0,len(arr))
	user.u_name = arr[temp] + '-' + str(random.randrange(10,100))

	user.save()
	return HttpResponse('添加用户成功:' + user.u_name)


def addgood(request):
	goods = Goods()
	arr = ['iphone','iPad','MacBook Pro','MacBook Air']
	temp = random.randrange(0,len(arr))
	goods.g_name = arr[temp] + '-' + str(random.randrange(0,10))
	goods.g_price = random.randrange(10000,100000)
	goods.save()
	return HttpResponse('商品添加成功' + goods.g_name)


def addcart(request):
	user = User.objects.last()

	# 将最后一件商品添加到改用户购物车中
	goods = Goods.objects.last()

	# 添加到关系表中
	goods.g_collection.add(user)
	return HttpResponse('【{}】添加{}购物车成功'.format(user.u_name,goods.g_name))


def showcart(request):
	# 一个用户  对应  多个商品(购物车)
	# 主表获取从表信息
	# 先选定用户，用户类没有物品属性，需要用到物品_set集合
	user = User.objects.last()

	# 商品列表
	good_list = user.goods_set.all()

	response_str = '<h1>{}购物车</h1>'.format(user.u_name)
	for goods in good_list:
		response_str += '<p>商品名:{},商品价格:{}</p>'.format(goods.g_name,goods.g_price)
	return HttpResponse(response_str)


def addcollect(request):
	goods = Goods.objects.last()
	user = User.objects.last()

	# 添加收藏
	goods.g_collection.add(user)
	return HttpResponse('商品{}被【{}】收藏'.format(goods.g_name,user.u_name))


def showgoods(request):
	goods_list = Goods.objects.all()

	response_str = ''
	for goods in goods_list:
		# 获取用户
		# 一个商品 对应 多个用户
		users = goods.g_collection.all()
		response_str += '<p>【收藏：{}】商品名:{},商品价格:{}</p>'.format(users.count(),goods.g_name, goods.g_price)
	return HttpResponse(response_str)
