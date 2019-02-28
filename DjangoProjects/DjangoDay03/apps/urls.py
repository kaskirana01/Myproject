from django.conf.urls import url

from apps import views

urlpatterns = [
	url(r'^index/$', views.index),
	url(r'^$', views.index),
	url(r'^animal/$', views.animal),
	url(r'^addanimal/$', views.addanimal),
	url(r'^selectanimal/$', views.selectanimal),
	url(r'^deleteanimal/$', views.deleteanimal),
	url(r'^updateanimal/$', views.updateanimal),
	url(r'^onetoone/$', views.onetoone),
	url(r'^addperson/$', views.addperson),
	url(r'^bindcard/$', views.bindcard),
	url(r'^deleteperson/$',views.deleteperson),
	url(r'^deleteIDcard/$',views.deleteIDcards),
	url(r'^getperson_card/$',views.getperson_card),
	url(r'^getcard_person/$',views.getcard_person),
	url(r'^onetomany/$', views.onetomany),
	url(r'^addgrade/$', views.addgrade),
	url(r'^addstudent/$', views.addstudent),
	url(r'^delgrade/$', views.delgrade),
	url(r'^delstudent/$', views.delstudent),
	url(r'^getgrade_stu/$',views.getgrade_stu), # 班级对应的学生
	url(r'^getstu_grade/$',views.getstu_grade) , # 显示学生对应的班级
	url(r'^manytomany/$',views.manytomany),
	url(r'^adduser/$',views.adduser),
	url(r'^addgood/$',views.addgood),
	url(r'^addcart/$',views.addcart),
	url(r'^showcart/$', views.showcart),
	url(r'^addcollect/$',views.addcollect),
	url(r'^showgoods/$', views.showgoods),

]
