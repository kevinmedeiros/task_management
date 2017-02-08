from django.shortcuts import render, redirect
from .admin import UserCreationForm
from rest_framework import viewsets
from .models import Task, GroupTask
from .serializers import TaskSerializer, GroupTaskSerializer


def home(request):
    return render(request, "home.html")


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home/')
        else:
            form = UserCreationForm()
            args = {'form': form}
            return render(request, 'registration/reg_form.html', args)


class TaskViewSet(viewsets.ModelViewSet):

    queryset = Task.objects.all().order_by('-title')
    serializer_class = TaskSerializer


class TaskGroupViewSet(viewsets.ModelViewSet):

    queryset = GroupTask.objects.all().order_by('-name')
    serializer_class = GroupTaskSerializer
