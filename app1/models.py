from email import message
from django.db import models 
# from phone_field import PhoneField
# Create your models here.


class FREE_CONSULATION (models.Model):
    name = models.CharField(max_length=250)
    phone = models.CharField(validators = [], max_length = 12)
    topics = models.fields
    message = models.TextField()
    data_create = models.DateTimeField(auto_now=True)


class email_address (models.Model):
    email = models.EmailField()
    data_create = models.DateTimeField(auto_now=True)




