from django.db import models

#自定义管理器
from django.db.models import Manager

class AnimalManager(Manager):
	# 重写父类方法
	# 默认删除逻辑删除的数据
	def all(self):
		return super().all().exclude(is_del=True)

########################################

# Create your models here.
class Animal(models.Model):
	name = models.CharField(max_length=40)
	age = models.IntegerField()

	# 逻辑删除
	is_del = models.BooleanField(default=False)

	# 如果没有自定义，系统默认objects
	# objects = models.Manager()
	myObjects = AnimalManager()

#########################################
# 一对一
# （主从表）明确不同的关系，不同的关系是如何实现的，数据删除时要怎么处理
# 一对一的关系
# 人和身份证 【一个人 对应 一个身份证号】

# 主表
# 人
class Person(models.Model):
	p_name = models.CharField(max_length=40)

# 从表
'''
create table apps_idcard
(
  id          int auto_increment
    primary key,
  i_no        varchar(40)  not null,
  i_sex       int          not null,
  i_addr      varchar(100) not null,
  i_person_id int          not null,
  constraint i_person_id
    unique (i_person_id),
  constraint apps_idcard_i_person_id_249d3f7b_fk_apps_person_id
    foreign key (i_person_id) references apps_person (id)
);
'''
# 主表数据删除,关联的从表数据，默认是会被删除的
# 身份证
class IDCard(models.Model):
	# 身份证号
	i_no = models.CharField(max_length=40)
	# 性别(1,男;2,女）
	i_sex = models.IntegerField()
	# 地址
	i_addr = models.CharField(max_length=100)

	# 声明关系(这个身份证是属于哪个人的）
	i_person = models.OneToOneField(Person)


	# 删除模式(在声明关系中写入参数）

	# 1.默认模式:models.CASCADE 主表数据删除，有无级联数据(从表)都会被删除
	# i_person = models.OneToOneField(Person, models.CASCADE)

	# 2.保护模式:models.PROTECT 主表数据删除，有级联数据，会抛出异常ProtectedError
	#                                   没有级联数据，主表数据直接删除
	# i_person = models.OneToOneField(Person,models.PROTECT)

	# 3.置空模式: models.SET_NULL 主表数据删除，有级联数据(从表)关系字段设置为NULL
	#                                       没有数据直接删除主表
	# i_person = models.OneToOneField(Person,models.SET_NULL,null=True)

	# 4.设置默认模式: models.SET_DEFAULT
	# i_person = models.OneToOneField(Person,models.SET_DEFAULT,default=1)

#######################################
# 一对多
# 一个班级 对应  多个学生
# 主表
class Grade(models.Model):
	g_name = models.CharField(max_length=40)

# 从表(声明关系)
"""
create table apps_student
(
  id         int auto_increment
    primary key,
  s_name     varchar(40) not null,
  s_age      int         not null,
  s_grade_id int         not null,
  constraint apps_student_s_grade_id_ef664023_fk_apps_grade_id
    foreign key (s_grade_id) references apps_grade (id)
);
"""
class Student(models.Model):
	s_name = models.CharField(max_length=40)
	s_age = models.IntegerField()

	# 声明关系(这学生 属于哪个班）
	# 班级删除后,学生不能删除,置为空.
	s_grade= models.ForeignKey(Grade,models.SET_NULL,null=True)

#######################################
# 多对多
# 用户 和 商品 多对多

# 一个用户 对应 多个商品（购物车)
# 一个商品 对应 被多个用户收藏

# 主表
class User(models.Model):
	u_name = models.CharField(max_length=40)

# 从表(声明关系)
class Goods(models.Model):
	g_name = models.CharField(max_length=40)
	g_price = models.IntegerField()

	# 多对多关系
	g_collection= models.ManyToManyField(User)

# 关系表(系统帮我们维护，后续都是自己手动维护）
"""
create table apps_goods_g_collection
(
  id       int auto_increment
    primary key,
  goods_id int not null,
  user_id  int not null,
  constraint apps_goods_g_collection_goods_id_user_id_10fc0372_uniq
    unique (goods_id, user_id),
  constraint apps_goods_g_collection_goods_id_eb07cfcb_fk_apps_goods_id
    foreign key (goods_id) references apps_goods (id),
  constraint apps_goods_g_collection_user_id_b63d9351_fk_apps_user_id
    foreign key (user_id) references apps_user (id)
);"""