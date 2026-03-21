from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Task


def register_page(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == "POST":
        username = request.POST.get('username', '').strip()
        password = request.POST.get('password', '')
        confirm  = request.POST.get('confirm_password', '')

        if not username or not password:
            return render(request, 'register.html', {'error': 'All fields are required'})

        if password != confirm:
            return render(request, 'register.html', {'error': 'Passwords do not match'})

        if len(password) < 8:
            return render(request, 'register.html', {'error': 'Password must be at least 8 characters'})

        if User.objects.filter(username=username).exists():
            return render(request, 'register.html', {'error': 'Username already taken'})

        User.objects.create_user(username=username, password=password)
        return redirect('login')

    return render(request, 'register.html')


def login_page(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == "POST":
        username = request.POST.get('username', '').strip()
        password = request.POST.get('password', '')

        if not username or not password:
            return render(request, 'login.html', {'error': 'All fields are required'})

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            return redirect('home')

        return render(request, 'login.html', {'error': 'Invalid username or password'})

    return render(request, 'login.html')


@login_required
def home(request):
    tasks = Task.objects.filter(user=request.user)
    query = request.GET.get('q', '').strip()
    if query:
        tasks = tasks.filter(title__icontains=query)
    count = tasks.filter(complete=False).count()
    return render(request, 'home.html', {'tasks': tasks, 'count': count})

@login_required
def add_task(request):
    if request.method == "POST":
        title = request.POST.get('title', '').strip()

        if not title:
            return render(request, 'add.html', {'error': 'Title is required'})

        Task.objects.create(
            user=request.user,
            title=title,
            description=request.POST.get('description', '').strip(),
        )
        return redirect('home')

    return render(request, 'add.html')


@login_required
def toggle_task(request, id):
    task = get_object_or_404(Task, id=id, user=request.user)

    if request.method == "POST":
        task.complete = not task.complete
        task.save()

    return redirect('home')


@login_required
def delete_task(request, id):
    task = get_object_or_404(Task, id=id, user=request.user)

    if request.method == "POST":
        task.delete()
        return redirect('home')

    return render(request, 'delete.html', {'task': task})

def logout_page(request):
    if request.method == "POST":
        logout(request)
    return redirect('/')
