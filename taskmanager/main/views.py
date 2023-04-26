from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm

def index(request):
    tasks=Task.objects.order_by('-id')
    return render(request,'main/index.html' , {'title': 'Главная страница сайта','tasks':tasks})


def about(request):
    return render(request, 'main/about.html')


def create(request):
    if request.method == 'POST':
        form = TaskForm(request.post)
        if form.is_valid():
            form.save()
            redirect('home')
        else:
            error = 'Invalid Form'

    form = TaskForm()
    context = {
        'form': form
    }
    return render(request, 'main/create.html')

