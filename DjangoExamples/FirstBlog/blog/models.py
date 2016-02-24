from django.db import models

# Create your models here.
class posts(models.Model):
    author = models.CharField(max_length=30)
    title = models.CharField(max_length=100)
    bodytext = models.TextField()
    timestamp = models.DateTimeField()
    
class users(models.Model):
    user_name = models.CharField(max_length=30)
    contact_no = models.IntegerField()
    password = models.CharField(max_length=30)
    email_id = models.CharField(max_length=50)
    address = models.TextField()
    
    