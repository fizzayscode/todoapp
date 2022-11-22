from django.db import models
import uuid
from django.contrib.auth.models import AbstractUser
from django.utils.timezone import datetime



class User(AbstractUser):
    id=models.UUIDField(default=uuid.uuid4,unique=True,primary_key=True,editable=False)
    name=models.CharField(max_length=100)
    email= models.EmailField(unique=True,null=True)
    avatar= models.ImageField(default="profile.png")

    USERNAME_FIELD= 'email'
    REQUIRED_FIELDS=['username']


class Task(models.Model):
    id=models.UUIDField(default=uuid.uuid4,unique=True,primary_key=True,editable=False)
    # setting null and blank to true because testing the application dont want to run into migration issues
    user= models.ForeignKey(User,on_delete=models.CASCADE,null=True, blank=True)
    name=models.CharField(max_length=100)
    description=models.TextField(null=True,blank=True)
    completed=models.BooleanField(default=False)
    created= models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

# model meta is used to chnage the behaviour of a class maybe the way i want to order it or chnage its name
    class Meta:
        # i want to order my class task based on the completed status// ordering a query set
        # whenever we are returning multiple items order it by the completed 
        ordering= ['completed']




