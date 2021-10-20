from django.db import models

# Create your models here.
class Notes(models.Model):
    title=models.CharField(max_length=100,blank=True)   
    note=models.TextField(blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True,blank=True,null=True)
    modified_at = models.DateTimeField(auto_now=True,blank=True,null=True)

   

class Users(models.Model):
    name=models.CharField(max_length=100,blank=True)
    username=models.CharField(max_length=100,blank=True)
    password=models.CharField(max_length=100,blank=True)
    email=models.CharField(max_length=100,blank=True)

   
    
