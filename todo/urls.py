from django.http import HttpResponse
from django.shortcuts import render
from django.urls import path
from . import views

urlpatterns = [

    # Add Task Url
    path('addTask',views.addTask,name='addtask'),

    # Mark Done Url
    path('mark_as_done/<int:pk>/',views.mark_as_done,name='mark_as_done'),

    # Mark Undone Url
    path('mark_as_undone/<int:pk>/',views.mark_as_undone,name='mark_as_undone'),

    # Edit Todo Task Url
    path('edit_task/<int:pk>/',views.edit_task,name='edit_task'),

    # Delete Todo Task Url 
    path('delete_task/<int:pk>',views.delete_task,name='delete_task')
]
