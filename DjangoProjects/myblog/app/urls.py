from django.conf.urls import url

from app import views

urlpatterns = [
	url(r'^$',views.index,name='index'),
	url(r'^signin$',views.signin,name='signin'),
	url(r'^mine/$',views.mine,name='mine'),
	url(r'^logout/$',views.logout,name='logout')
]