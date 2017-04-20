from django.db import models

# Create your models here.
class user(models.Model):
	wxid = models.CharField(max_length=20,primary_key=True)
	uclass = models.ManyToManyField(Class)

class School(models.Model):
	schoolid = models.CharField(max_length=20,primary_key=True)
	schoolname = models.CharField(max_length=20)

class Class(models.Model):
	classid =  models.CharField(max_length=20,primary_key=True)
	schoolbelong = models.ForeignKey(School)