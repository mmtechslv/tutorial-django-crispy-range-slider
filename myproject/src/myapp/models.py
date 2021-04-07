from django.db import models

class People(models.Model):
    name = models.CharField(null=True,blank=True,max_length=50)
    surname = models.CharField(null=True,blank=True,max_length=50)
    age = models.IntegerField()
