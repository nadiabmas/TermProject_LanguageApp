from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def dashboard(request):
    return render(request, 'dashboard.html')


def error_language(request):
    return render(request, 'error_language.html')


def lessons(request):
    return render(request, 'lessons.html')


def quizzes(request):
    return render(request, 'quizzes.html')


def progress(request):
    return render(request, 'progress.html')


