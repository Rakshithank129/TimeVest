from django.shortcuts import render,redirect
from taskmanagement.forms import taskForm
from taskmanagement.models import tasks
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

@login_required(login_url="login")
def taskmanagement(request):
    form = taskForm()

    # collecting all the task detils belongs to tasks model
    alltasks = tasks.objects.all()
    paginator = Paginator(alltasks,3)
    page = request.GET.get('pg')
    alltasks = paginator.get_page(page)

    if request.method == 'POST':
        form = taskForm(request.POST) # to access the data entered html to views.py
        if form.is_valid():
            form.save()
            print("data saved")

    context = {
        'form':form,
        'alltasks':alltasks
    }
    return render(request,'taskmanagement.html',context)

@login_required(login_url="login")
def edit_task(request,id=0):
    one_task = tasks.objects.get(pk=id)
    if request.method == 'POST':
        form = taskForm(request.POST,instance=one_task)
        if form.is_valid():
            form.save()
            return redirect("alltasks")
    else:
        form = taskForm(instance=one_task)
    return render(request,"edittask.html",{'form':form})

def delete_task(request,id=0):
    new_task = tasks.objects.get(pk=id)
    new_task.delete()
    return redirect("alltasks")