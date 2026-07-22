from django.http import HttpResponse
from django.shortcuts import render
from django.urls import path
from . import views

urlpatterns = [
    path('addTask',views.addTask,name='addtask')
]
