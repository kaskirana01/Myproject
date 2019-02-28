# 配置文件

import re
import views
urlpatterns = [
	(r'^$',views.index),
	(r'^login$',views.login),
	(r'^dologin$',views.doLogin),
	(r'^studentlist$',views.studentList),
	(r'^studentlist/(\d+)$',views.studentInfo),
	# (r'^complain$',views.complain)
	(r'^register$',views.register),
	(r'^static/',views.loadStatic),
	(r'^yzm',views.yzm),
]