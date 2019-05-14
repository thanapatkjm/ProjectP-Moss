from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User  #username , password , email
from datetime import datetime    

class UserPoints(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    points = models.IntegerField(default=0)
