from django.db import models

class Animal(models.Model):
	name = models.CharField(max_length=100,default='')
	color = models.CharField(max_length=40,default='')

	# 设置元选项 告诉系统，此表不需要
	class Meta:
		abstract = True # 抽象化

class Cat(Animal):

	eat = models.CharField(max_length=100)

class Dog(Animal):
	# name = models.CharField(max_length=100)
	# color = models.CharField(max_length=40)
	eat = models.CharField(max_length=100)
	speak = models.CharField(max_length=100)

class Fish(Animal):
	# name = models.CharField(max_length=100)
	# color = models.CharField(max_length=40)
	swim = models.CharField(max_length=100)

class Snake(Animal):
	# name = models.CharField(max_length=100)
	# color = models.CharField(max_length=40)
	sleep = models.CharField(max_length=100)