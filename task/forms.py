from django import forms
from task.models import Task
from django.contrib.auth.forms import User

class RegistrationForm(forms.ModelForm):
    class Meta:
        model=User
        fields=["username","password","email"]

class LoginForm(forms.Form):
    # password=forms.CharField(write_only=True)
    username=forms.CharField(max_length=50)
    password=forms.CharField(widget=forms.PasswordInput)

class TaskAddForm(forms.ModelForm):
    # id=forms.CharField(read_only=True)
    class Meta:
        model=Task
        fields="__all__"

class FilterAddForm(forms.ModelForm):
    class Meta:
        model=Task
        fields=["priority"]