from django.contrib import admin
from .models import *


class TodoAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug', 'day_created')
    list_display_links = ('id', 'name', 'slug')
    prepopulated_fields = {'slug' : ('name',)}

admin.site.register(TodoList, TodoAdmin)