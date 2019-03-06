from django.contrib import admin

# Register your models here.

from app.models import Goods, Grade, Student

# 注册 添加 app
# 自定义操作
class GoodsAdmin(admin.ModelAdmin):
	# 显示的字段
	list_display = ['pk','name','icon','price']

	# 分页
	list_per_page = 10

	# 过滤字段
	list_filter = ['name']

	# 搜索字段
	search_fields = ['name','pk']

	# 执行动作位置
	actions_on_top = False   # 动作按钮跑底部去了
	actions_on_bottom = True

admin.site.register(Goods,GoodsAdmin)

class StudentInfo(admin.TabularInline):
	model = Student
	extra = 1

class GradeAdmin(admin.ModelAdmin):
	list_display = ['id','g_name']
	# 设置级联对象   班级界面可以添加同学
	inlines = [StudentInfo]

class StudentAdmin(admin.ModelAdmin):
	list_filter = ['s_grade']
	list_display = ['id','s_name','s_score']

admin.site.register(Grade,GradeAdmin)
admin.site.register(Student,StudentAdmin)