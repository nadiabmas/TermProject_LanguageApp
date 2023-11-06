from django.shortcuts import render, redirect
from .models import UserProfile
from .forms import SignInForm


def index(request):
    if request.method == 'POST':
        form = SignInForm(data=request.POST)
        if form.is_valid():
            return redirect('pick_language')
    else:
        form = SignInForm()
    return render(request, 'index.html', {'form': form})


def pick_language(request):
    return render(request, 'pick_language.html')


def error_language(request):
    return render(request, 'error_language.html')


def dashboard(request):
    return render(request, 'dashboard.html')


def lessons(request):
    return render(request, 'lessons.html')


def quizzes(request):
    return render(request, 'quizzes.html')


def progress(request):
    return render(request, 'progress.html')
