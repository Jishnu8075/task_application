from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Task(models.Model):
    title=models.CharField(max_length=20,unique=True)
    description=models.CharField(max_length=50)
    options=(
        ("High","High"),
        ("Medium","Medium"),
        ("Low","Low")
    )
    priority=models.CharField(max_length=50,choices=options,default="Medium")
    options=(
        ("pending","pending"),
        ("inprogress","inprogress"),
        ("completed","completed")
    )
    status=models.CharField(max_length=50,choices=options,default="inprogress")



