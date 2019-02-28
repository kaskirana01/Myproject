from django.conf.urls import url

from Stu_info import views

urlpatterns = [
	url(r'^$',views.index),
	url(r'^index/$',views.index),
	url(r'^addStu/$',views.addStu),
	url(r'^delStu/$',views.delStu),
	url(r'^delall/$',views.delall),
	url(r'^showallStu/$',views.showallStu)
]