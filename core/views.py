from django.shortcuts import render, redirect
from .admin import UserCreationForm


def home(request):
    return render(request, "home.html")


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('')

    else:
        form = UserCreationForm()

        args = {'form': form}
        return render(request, 'registration/reg_form.html', args)

