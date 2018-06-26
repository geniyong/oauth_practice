from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,redirect, render_to_response
from .models import *

from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse
from django.http import HttpResponseRedirect

def loginView(request):
    if request.method =="GET":
        pass

    elif request.method == 'POST':
        pass
    return render(request, 'myApp/login.html')

