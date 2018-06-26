from django.contrib.auth import login
from django.core.files import temp
from django.urls import path, re_path
from .views import *

urlpatterns = [
    re_path(r'^login/$', loginView, name='login'),
    ]