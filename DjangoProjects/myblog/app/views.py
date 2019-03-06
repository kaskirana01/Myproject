from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
# 首页
from app.models import User


def index(request):
	return render(request,'index.html')


# 注册
def signin(request):
	if request.method == 'GET':
		return render(request,'signin.html')
	elif request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')
		sex = request.POST.get('sex')
		money = request.POST.get('money')
		E_mail = request.POST.get('E_mail')
		try:
			user = User()
			user.username = username
			user.password = password
			user.sex = sex
			user.money = money
			user.E_mail = E_mail
			print(user.username,user.password,user.money,user.sex,user.E_mail)
			user.save()
			response = render(request,'mine.html',context={'username':username})
			response.session['session_data']=user.username
			return  response
		except Exception as e:
			print(e)
			return HttpResponse('注册失败！请重新注册!')
		# print(user.username,user.password,user.money,user.sex,user.E_mail)

# 登录成功跳转
def mine(request):
	if request.method != 'POST':
		return render(request,'index.html',context={'err':'登录失败，请重试！'})

	elif request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')

		# 验证
		users = User.objects.filter(username=username)

		if users.exists():
			user = users.first()
			if user.password == password:
				return render(request,'mine.html',context={'username':username})
			else:
				return render(request, 'index.html', context={'err': 'Login failed, please try again'})

		else:
			return render(request,'signin.html',context={'unknown_user':'Unknowm_User,Please Signin'})


def logout(request):
	pass