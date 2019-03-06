from django.db import models

# Create your models here.
class User(models.Model):
	username = models.CharField(max_length=40,unique=True)
	password = models.CharField(max_length=100)
	sex = models.CharField(max_length=10)
	money = models.CharField(max_length=100)
	E_mail = models.CharField(max_length=100)
