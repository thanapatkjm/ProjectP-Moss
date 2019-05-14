from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User  #username , password , email
from datetime import datetime    

class UserPoints(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    points = models.IntegerField(default=0)

class UserLog(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    datetime = models.DateTimeField(default=datetime.now)
    type = models.TextField()
    weight = models.TextField()
    points = models.IntegerField()