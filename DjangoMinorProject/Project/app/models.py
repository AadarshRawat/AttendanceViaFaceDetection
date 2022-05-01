from django.db import models
import datetime
# Create your models here.

class Student(models.Model):
    rollnumber=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    lname=models.CharField(max_length=100)
    attendance=models.IntegerField(default=0)
    time_of_attendance=models.DateTimeField(auto_now=True)

