from django.db import models
'''
# 字段类型
- CharField 字符串
- IntegerField 整形
- AutoField 自增长（整形）
- FloatField 浮点数
- DecimalField  指定小数长度
- TextField 大文本字符串
- BooleanField  布尔类型
- DateField  只有日期
- TimeField  只有时间
- DateTimeField  时间和日期

# 约束
- primary_key = True 主键
- max_length  最大长度
- null  是否为空（默认是not null）
- auto_now  每次更新的时间
- auto_now_add  记录被创建时的时间
- decimal_places 小数点保留几位
- max_digits  总长度
- blank 是否为空值
- default 默认值

# 关系
- OneToOneField 一对一
- ForeginKey 一对多
- MantToManyField  多对多
'''

# Create your models here.
class student(models.Model):
	s_id = models.AutoField(primary_key=True)
	# s_id = models.AutoField(primary_key=True)
	s_name = models.CharField(max_length=100)
	# s_name = models.CharField(max_length=100)
	s_score = models.IntegerField(null=True)
	# s_score = models.IntegerField(null=True)
	s_weight = models.FloatField(null=True)
	# s_weight = models.FloatField(null=True)
	s_height = models.DecimalField(max_digits=6,decimal_places=2)
	# s_height = models.DecimalField(max_digits=6,decimal_places=2)
	s_detil = models.TextField(default='')
	# s_detil = models.TextField(default='')
	s_delete = models.BooleanField(default=False)
	# s_delete = models.BooleanField(default=False)
	s_create = models.DateTimeField(auto_now_add=True)
	# s_create = models.DateTimeField(auto_now_add=True)
	s_change = models.DateTimeField(auto_now=True)
	# s_change = models.DateTimeField(auto_now=True)
	s_test = models.IntegerField(null=True)
	# s_test = models.IntegerField(null=True)

	s_math = models.IntegerField(default=0)
	# s_math = models.IntegerField(default=0)
	s_english = models.IntegerField(default=0)
	# s_english = models.IntegerField(default=0)

	# 元选项
	# 设置自定义表名，改为student
	class Meta:
	# class Meta:
		db_table = 'student'
		# ordering = ['s_score']
		# 系统默认情况下按id升序排序，可以改为成绩升序，等等
		ordering = ['s_score']