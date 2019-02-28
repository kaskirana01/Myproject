from django.conf.urls import url

from meituan import views

urlpatterns = [

    url(r'^meituan/$', views.index),
    url(r'^$', views.index),
    url(r'^addstu/$', views.addStu),
    url(r'^changestu/$', views.changestu),
    url(r'^showstudents/$', views.showstudents),
    url(r'^showstu/$', views.showstu),
    url(r'^agg/$',views.agg),
    url(r'^qtest/$',views.Qtest),
    url(r'^ftest/$',views.Ftest),

]