from django.shortcuts import render, redirect
from django.contrib import messages

from .models import ToDO
from .forms import TodoForm

def add_view(request):
    item_list = ToDO.objects.all()
    if request.method == 'POST':
        form = TodoForm(request.POST or None)
        if form.is_valid():
           form.save()
        return redirect('add')
    form = TodoForm()
    context = {
        'form':form,
        'list':item_list,
        'title':"To-Do-List"
    }
    return render(request,'todo/add.html',context)

def update_task_view(request, pk):
    task = ToDO.objects.get(id = pk)
    form = TodoForm(instance = task)
    if request.method == 'POST':
        form = TodoForm(request.POST, instance = task)
        if form.is_valid():
           form.save()
        return redirect('/')
    context = {
        'form': form
    }
    return render(request, 'todo/update_task.html', context)

def remove_view(request, pk):
    item = ToDO.objects.get(id = pk)
    if request.method == 'POST':
        item.delete()        
        return redirect('/')
    context = {
        'item': item
    }
    return render(request, 'todo/delete.html', context)