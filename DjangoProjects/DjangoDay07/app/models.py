from django.db import models

# Create your models here.
"""
id     | int(11)      | NO   | PRI | NULL    | auto_increment |
| name   | varchar(20)  | NO   |     | NULL    |                |
| icon   | varchar(255) | NO   |     | NULL    |                |
| price  | int(11)      | NO   |     | NULL    |                |
| detail | varchar(255) | NO   |     | NULL    |
"""
class Goods(models.Model):
	name = models.CharField(max_length=20)
	icon = models.CharField(max_length=255)
	price = models.IntegerField()
	detail = models.CharField(max_length=255)

	class Meta:
		db_table = 'goods'

	# 定制后台显示
	# def __str__(self):
	# 	return self.name

class Grade(models.Model):
	g_name = models.CharField(max_length=40)

	# 定制后台显示
	def __str__(self):
		return self.g_name

class Student(models.Model):
	s_name = models.CharField(max_length=40)
	s_score = models.IntegerField()

	s_grade = models.ForeignKey(Grade)
