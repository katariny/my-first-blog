"""mysite URL Configuration

[...]
"""
from django.contrib import admin
from django.urls import path, include



urlpatterns = [  #cria urls dos sites#
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),

]
