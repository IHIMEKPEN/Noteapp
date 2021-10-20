from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Notes(models.Model):
    title=models.CharField(max_length=100,blank=True)   
    note=models.TextField(blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True,blank=True,null=True)
    modified_at = models.DateTimeField(auto_now=True,blank=True,null=True)
    user=models.ForeignKey('User' ,on_delete=models.CASCADE,related_name='noelated',null=True)

   

class User(AbstractUser):
    pass

   
    
