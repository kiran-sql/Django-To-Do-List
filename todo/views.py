from django.shortcuts import render, redirect
from django.contrib import messages

from .models import ToDO
from .forms import TodoForm

def add_view(request):
    item_list = ToDO.objects.order_by('-time')
    if request.method == 'post':
        form = TodoForm(request.post)
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

def remove_view(request):
    item = ToDO.objects.get(id=item_id)
    item.delete()
    messages.info(request, "item removed !!!")
    return redirect('add')
    # return render(request,'todo/remove.html')