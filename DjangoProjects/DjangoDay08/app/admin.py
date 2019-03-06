from django.contrib import admin

# Register your models here.
from app.models import News, Book

admin.site.register(News)
admin.site.register(Book)