from django.shortcuts import render
from home.models import Task

# Create your views here.
def home (request):
    context = {'success': False}
    if request.method == 'POST':
        title = request.POST['title']
        desc = request.POST ['desc']
        print(title,desc)
        ist = Task(taskTitle = title, taskDesc = desc)
        ist.save()
        context = {'success': True}
        
    return render (request,'index.html',context)
def task (request):
    alltasks = Task.objects.all()
 
    context = {'tasks': alltasks}
    return render (request, 'task.html',context)