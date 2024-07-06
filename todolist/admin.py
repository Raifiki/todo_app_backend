from django.contrib import admin

from todolist.models import TodoList

class AdminTodoList(admin.ModelAdmin):
    list_display = ['title']

# Register your models here.

admin.site.register(TodoList,AdminTodoList)
