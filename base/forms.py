from django.forms import ModelForm
from .models import Task,User
from django.contrib.auth.forms import UserCreationForm


class TaskForm(ModelForm):
    class Meta:
        model=Task
        fields=['name','description','completed']


class RegisterForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username','email','name','password1','password2']
