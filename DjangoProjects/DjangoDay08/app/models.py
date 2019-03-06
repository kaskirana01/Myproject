from django.db import models

# Create your models here.
from tinymce.models import HTMLField


class News(models.Model):   # 富文本
	n_title = models.CharField(max_length=100)
	n_time = models.DateTimeField(auto_now=True)

	# 富文本定制
	# n_content = models.TextField()
	n_content = HTMLField()    # 需要导包

	def __str__(self):
		return self.n_title

class Book(models.Model):   # md文本
	b_title = models.CharField(max_length=100)
	b_time = models.DateTimeField(auto_now=True)
	b_content = models.TextField()

	def __str__(self):
		return self.b_title