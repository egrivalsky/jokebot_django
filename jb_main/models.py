from django.db import models
from datetime import date
from django.contrib.auth.models import User

# Create your models here.

class Joke(models.Model):
    text = models.TextField()
    source = models.CharField(blank=True, max_length=50, default='unknown')
    author = models.CharField(blank=True, max_length=50, default='unknown')
    frequency = models.IntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    print('THIS IS THE USER VVVVVVVV')
    print(user)
    print('THAT WAS THE USER ^^^^^^^^^^^^')


    def __str__(self):
        return self.author

class Profile(models.Model):
    about_me = models.CharField(blank=True, max_length=500)
    twitter_handle = models.CharField(blank=True, max_length=50)
    twitter_password = models.CharField(max_length=32)

class OldJoke(models.Model):
    text = models.TextField()
    source = models.CharField(blank=True, max_length=50)
    author = models.CharField(blank=True, max_length=50)
    frequency = models.IntegerField(default=0)