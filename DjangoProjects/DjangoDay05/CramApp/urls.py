from django.conf.urls import url

from CramApp import views

urlpatterns = [
	url(r'^$',views.index,name='index'),

	#正则表达式 () 表示一个分组 对应一个参数
	url(r'^goods/$',views.goods,name='goods'),  # 没带参数默认第一页
	url(r'^goods/(\d+)/$',views.goods,name='goodslist'),

	# 路径参数路由
	url(r'^sum/(\d+)/(\d+)/(\d+)/$',views.sum,name='sum'),

	# <> 标识清楚参数名 \w 字母加数字  ?P 表示python
	url(r'^detail/(?P<name>\w+)/$',views.detail,name='detail'),

	url(r'^gettest/$',views.gettest,name='gettest'),
	url(r'^postview/$',views.postview,name='postview'),
	url(r'^posttest/$',views.posttest,name='posttest'),

	url(r'^urltest/$',views.urltest,name='urltest'),
	url(r'^jsontest/$',views.jsontest,name='jsontest'),


	url(r'^register/$',views.register,name='register'),
	url(r'^logout/$',views.logout,name='logout'),
	url(r'^login/$',views.login,name='login'),
]