from django.contrib import admin

from todolist.models import TodoItem

class AdminTodoItem(admin.ModelAdmin):
    list_display = [
        'id',
        'title','checked',
        'author',
        'created_at',
        ]

# Register your models here.

admin.site.register(TodoItem,AdminTodoItem)
