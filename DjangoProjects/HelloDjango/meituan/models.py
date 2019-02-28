from django.db import models

# Create your models here.
# 学生 模型类 链接数据库
# 默认 appName_ModelName
class Student(models.Model):
	name = models.CharField(max_length=100)  # varchar字符串类型
	score = models.IntegerField()

class User(models.Model):
	username = models.CharField(max_length=100)
	password = models.CharField(max_length=100)