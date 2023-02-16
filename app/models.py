from django.db import models

# Create your models here.

class student(models.Model):
    id=models.IntegerField(max_length=100,primary_key=True)
    name=models.CharField(max_length=100)
    age=models.IntegerField()
    