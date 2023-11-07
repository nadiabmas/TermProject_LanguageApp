from django.urls import path
from . import views

# Url direction of every html file in my app
urlpatterns = [
    path('', views.index, name='index'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('pick_language/', views.pick_language, name='pick_language'),
    path('error_language/', views.error_language, name='error_language'),
    path('lessons/', views.lessons, name='lessons'),
    path('quizzes/', views.quizzes, name='quizzes'),
    path('progress/', views.progress, name='progress'),
    path('quiz_1/', views.quiz_1, name='quiz_1'),
    path('quiz_2/', views.quiz_2, name='quiz_2'),
    path('quiz_3/', views.quiz_3, name='quiz_3'),
]
