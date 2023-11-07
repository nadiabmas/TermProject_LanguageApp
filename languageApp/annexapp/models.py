from django.db import models


# For database of user profile (includes: name, username, and password)
class UserProfile(models.Model):
    name = models.CharField(max_length=50)
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=50)

