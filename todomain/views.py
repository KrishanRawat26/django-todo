from django.shortcuts import render
from todo.models import Task
def home(request):
    task = Task.objects.filter(is_completed=False).order_by('-created_at')
    completed_task = Task.objects.filter(is_completed=True)
    #print(task)
    context = {
        'task':task,
        'completed_task':completed_task
    }
    return render(request,"home.html",context)