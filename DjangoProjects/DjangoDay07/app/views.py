import math

from django.core.cache import cache
from django.core.paginator import Paginator
from django.shortcuts import render

# Create your views here.
from django.views.decorators.cache import cache_page  # 缓存

from app.models import Goods


# 全部缓存cache_page
@cache_page(10)
def index(request,num=1):
	print('打印证明没有缓存###############################')
	# 手动分页
	goods_list = Goods.objects.all()
	goods_page = math.ceil(goods_list.count() / 12)

	# num第几页
	num = int(num)
	goods_list = Goods.objects.all()[(num - 1) * 12:num * 12]

	# 局部缓存
	# cache.set(key,value,timeout)
	cache.set('token','qwe1231oiu98ad89s79d81231uyr!!#',timeout = 10)

	return render(request,'index.html',context={
		'goods_list':goods_list,
		'goods_page':range(goods_page),
	})


def goods(request,num=1):
	goods_list = Goods.objects.all()

	# 缓存
	# value = cache.get(key)
	token = cache.get('token','不存在')
	print(token)
	# 分页对象(数据源,单页数据)
	paginator = Paginator(list(goods_list),12)

	# 获取当前页对象
	pageObj = paginator.page(num)
	return render(request,'goods.html',context={
		'pageObj':pageObj
	})