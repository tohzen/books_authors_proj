from django.db import models

# Create your models here.
class Show(models.Model):
    title= models.CharField(max_length=255)
    network= models.TextField(max_length=255, null=True )
    release_date= models.DateField(max_length=255, null=True)
    created_at= models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_now=True)
    
    
    
# class Author(models.Model):
#     first_name= models.CharField(max_length=255)
#     last_name= models.CharField(max_length=255)
#     Book= models.ManyToManyField(Book, related_name= "authors")
#     notes= models.TextField(max_length=255, null=True)
#     created_at= models.DateTimeField(auto_now_add=True)
#     updated_at= models.DateTimeField(auto_now=True)