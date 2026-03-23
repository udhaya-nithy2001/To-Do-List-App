from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Task

# DRF Imports
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .serializers import TaskSerializer


# ---------------- AUTH ---------------- #

def register_page(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == "POST":
        username = request.POST.get('username', '').strip()
        password = request.POST.get('password', '')
        confirm = request.POST.get('confirm_password', '')

        if not username or not password:
            return render(request, 'register.html', {'error': 'All fields are required'})

        if password != confirm:
            return render(request, 'register.html', {'error': 'Passwords do not match'})

        if len(password) < 8:
            return render(request, 'register.html', {'error': 'Password must be at least 8 characters'})

        if User.objects.filter(username=username).exists():
            return render(request, 'register.html', {'error': 'Username already taken'})

        user = User.objects.create_user(username=username, password=password)

        # Auto login after register (better UX)
        login(request, user)
        return redirect('home')

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


def logout_page(request):
    if request.method == "POST":
        logout(request)
    return redirect('login')


# ---------------- WEB VIEWS ---------------- #

@login_required(login_url='login')
def home(request):
    tasks = Task.objects.filter(user=request.user).order_by('complete', '-created_at')

    query = request.GET.get('q', '').strip()
    if query:
        tasks = tasks.filter(title__icontains=query)

    count = tasks.filter(complete=False).count()

    return render(request, 'home.html', {
        'tasks': tasks,
        'count': count
    })


@login_required(login_url='login')
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


@login_required(login_url='login')
def toggle_task(request, id):
    if request.method != "POST":
        return redirect('home')

    task = get_object_or_404(Task, id=id, user=request.user)
    task.complete = not task.complete
    task.save()

    return redirect('home')


@login_required(login_url='login')
def delete_task(request, id):
    task = get_object_or_404(Task, id=id, user=request.user)

    if request.method == "POST":
        task.delete()
        return redirect('home')

    return render(request, 'delete.html', {'task': task})


# ---------------- REST API ---------------- #

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def task_list_create(request):

    tasks = Task.objects.filter(user=request.user).order_by('-created_at')

    # 🔍 Search
    query = request.GET.get('q')
    if query:
        tasks = tasks.filter(title__icontains=query)

    if request.method == 'GET':
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = TaskSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=201)

        return Response(serializer.errors, status=400)


@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
@permission_classes([IsAuthenticated])
def task_detail(request, id):

    task = get_object_or_404(Task, id=id, user=request.user)

    if request.method == 'GET':
        serializer = TaskSerializer(task)
        return Response(serializer.data)

    elif request.method in ['PUT', 'PATCH']:
        serializer = TaskSerializer(task, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=400)

    elif request.method == 'DELETE':
        task.delete()
        return Response(status=204)