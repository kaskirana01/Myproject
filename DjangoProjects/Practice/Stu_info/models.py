from django.db import models

# Create your models here.
class Stu(models.Model):
	s_name = models.CharField(max_length=40)
	s_sno = models.IntegerField()
	s_sex = models.CharField(max_length=20)
	s_score = models.IntegerField()
