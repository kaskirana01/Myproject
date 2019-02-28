from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^eleme/$',views.eleme),
	url(r'^$',views.eleme)
]