from django.shortcuts import redirect, render
from .forms import *


# Sign in form
def index(request):
    if request.method == 'POST':
        form = SignInForm(data=request.POST)
        if form.is_valid():
            return redirect('pick_language')
    else:
        form = SignInForm()
    return render(request, 'index.html', {'form': form})


# Render html files
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


def quiz_1(request):
    return render(request, 'quiz_1.html')


def quiz_2(request):
    return render(request, 'quiz_2.html')


def quiz_3(request):
    return render(request, 'quiz_3.html')


def progress(request):
    return render(request, 'progress.html')
