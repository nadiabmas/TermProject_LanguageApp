from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('error_language/', views.error_language, name='error_language'),
    path('lessons/', views.lessons, name='lessons'),
    path('quizzes/', views.quizzes, name='quizzes'),
    path('progress/', views.progress, name='progress'),
]
