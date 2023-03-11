from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=100)
    roll=models.IntegerField()
    stream=models.CharField(max_length=100)
    subject=models.CharField(max_length=50)
    join_at=models.DateTimeField()
