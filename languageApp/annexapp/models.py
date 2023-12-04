from django.db import models


# For database of user profile (includes: name, username, and password)
class UserProfile(models.Model):
    name = models.CharField(max_length=50)
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=50)


class Quiz(models.Model):
    quiz_title = models.CharField(max_length=50)
    quiz_description = models.TextField(max_length=350)


class Question(models.Model):
    question_text = models.TextField(max_length=150)


class Option(models.Model):
    option_text = models.CharField(max_length=150)
    is_correct = models.BooleanField(True)


# class UserAnswer(models.Model):


