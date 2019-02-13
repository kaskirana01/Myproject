# 配置文件

import re
import views
urlpatterns = [
	(r'^$',views.index),
	(r'^login$',views.login),
	(r'^dologin$',views.doLogin),
	(r'^studentlist$',views.studentList),
	# (r'^complain$',views.complain)
]