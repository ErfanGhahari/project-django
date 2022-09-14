
from email.policy import default
from django.db import models

# Create your models here.

class comment(models.Model):
    name=models.CharField(max_length = 200)
    email=models.EmailField()
    text=models.TextField()
    message=models.TextField()
    data=models.DateTimeField(auto_now = True)
    picture=models.ImageField(upload_to = 'user_profile',default = 'some string')
     
    