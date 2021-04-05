from django.db import models
from datetime import date
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

class Joke(models.Model):
    text = models.TextField()
    source = models.CharField(blank=True, max_length=50, default='unknown')
    author = models.CharField(blank=True, max_length=50, default='unknown')
    frequency = models.IntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    last_tweeted = models.DateTimeField(auto_now=False, auto_now_add=False, blank=True, null=True)


    def __str__(self):
        return self.author

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    favorites = models.ManyToManyField(Joke)
    about_me = models.CharField(blank=True, max_length=500)
    twitter_handle = models.CharField(blank=True, max_length=50)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
    



class OldJoke(models.Model):
    text = models.TextField()
    source = models.CharField(blank=True, max_length=50)
    author = models.CharField(blank=True, max_length=50)
    frequency = models.IntegerField(default=0)