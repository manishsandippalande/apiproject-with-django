from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# User
# Client
# Project
# class UserProfile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)

# class userdata(models.Model):
#     name = models.CharField(max_length=30)

class clients(models.Model):
    name = models.CharField(max_length=20)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    creted_on = models.DateTimeField(auto_now_add=True)

class projects(models.Model):
    name = models.CharField(max_length=20)
    cname = models.ForeignKey(clients, on_delete=models.CASCADE)
    uname = models.ManyToManyField(User)
    creted_on = models.DateTimeField(auto_now_add=True)