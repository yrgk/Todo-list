from django.contrib import admin
from django.urls import path
from todo_list.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='home'),
    path('add', add_to_list, name='addtask'),
    path('<slug:post_slug>/complete/', complete, name='complete'),
    path('<slug:post_slug>/edit', edit, name='edit'),
]
