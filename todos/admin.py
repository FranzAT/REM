#todos/admin.py
#https://wsvincent.com/django-rest-framework-react-tutorial/

from django.contrib import admin

from .models import Todo


class TodoAdmin(admin.ModelAdmin):
    fields = ['title', 'description', 'user']


admin.site.register(Todo, TodoAdmin)
