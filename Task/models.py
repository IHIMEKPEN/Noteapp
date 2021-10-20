from django.db import models

# Create your models here.
class Notes(models.Model):
    title=models.CharField(max_length=100,blank=True)
    note=models.TextField(blank=True,null=True)
    # created_at = models.DateTimeField(auto_now_add=True,null=False,blank=True)
    # modified_at = models.DateTimeField(auto_now=True,null=False,blank=True)

    def __str__(self):
        return  self.note

    
