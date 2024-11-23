from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from .models import Task, SendInvitation
from .forms import TaskForm, SendInvitationForm

def home(request):
    if request.user.is_authenticated:
        return redirect('task_list')
    return render(request, "taskm/home.html")

def logout_view(request):
    logout(request)
    return redirect("home")

@login_required
def task_list(request):
    tasks = Task.objects.filter(user=request.user)
    return render(request, 'taskm/task_list.html', {'tasks': tasks})

@login_required
def create_task(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            return redirect('task_list')
    else:
        form = TaskForm()
    return render(request, 'taskm/create_task.html', {'form': form})

@login_required
def update_task(request, pk):
    task = get_object_or_404(Task, pk=pk, user=request.user)
    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm(instance=task)
    return render(request, 'taskm/update_task.html', {'form': form})

@login_required
def delete_task(request, pk):
    task = get_object_or_404(Task, pk=pk, user=request.user)
    if request.method == "POST":
        task.delete()
        return redirect('task_list')
    
def invite_user(request):
    if request.method == "POST":
        form = SendInvitationForm(request.POST)
        if form.is_valid():
            invitation = form.save()
            send_mail(
                "Join Now, The Best task management app☻",
                "Please use the following link to register: https://wellfound.com/company/ai47labs",
                "trials9999@gmail.com",
                [invitation.email], 
                fail_silently=False,
            )
            return redirect('admin:index')
    else:
        form = SendInvitationForm()
    return render(request, 'admin/invite_user.html', {'form': form})


    
