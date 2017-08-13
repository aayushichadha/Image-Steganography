from __future__ import unicode_literals
from django.db import models

# Create your models here.
class User(models.Model):
    user_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=200)
    key = models.CharField(max_length=200,null=True)

class Document(models.Model):
    description = models.CharField(max_length=255, blank=True)
    document = models.ImageField(upload_to='')
    uploaded_at = models.DateTimeField(auto_now_add=True)