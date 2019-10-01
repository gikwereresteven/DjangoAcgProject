from django.db import models
from django.conf import settings

# Create your models here.
class Post(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    message=models.TextField()
    
