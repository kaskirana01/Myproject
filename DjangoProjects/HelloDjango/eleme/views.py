from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from .models import users
import random

def eleme(request):
	man = users()
	man.name = '王五' + str(random.randrange(1,100))
	man.address = '湖北省' + str(random.randrange(1,100))
	man.save()
	return HttpResponse("饿了么增加用户" + man.name)