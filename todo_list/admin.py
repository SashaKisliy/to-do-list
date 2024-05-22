from django.contrib import admin
from todo_list.models import Task, Tag


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ("content", "created_at", "deadline", 'done')
    list_filter = ('done', 'created_at', 'deadline')
    search_fields = ('content',)
    ordering = ('done', '-created_at')


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
