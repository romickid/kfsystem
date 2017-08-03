from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted((item, item) for item in get_all_styles())

class Admin(models.Model):
    email=models.EmailField(max_length=200,default='null')
    nickname=models.CharField(max_length=100,blank=True, default='null')
    password=models.CharField(max_length=128, blank=True, default='null')

class CustomerService(models.Model):
    email=models.EmailField(max_length=200,default='null')
    nickname=models.CharField(max_length=100,blank=True, default='null')
    password=models.CharField(max_length=128, blank=True, default='null')

class ChattingLog(models.Model):
    client_id=models.CharField(max_length=100, blank=True, default='null')
    #service_id=models.ForeignKey(CustomerService)
    service_id=models.CharField(max_length=100, blank=True, default='null')
    content=models.CharField(max_length=500, blank=True, default='null')
    is_client=models.BooleanField(default=False)
    time=models.DateTimeField()

class SerialNumber(models.Model):
    serials=models.CharField(max_length=200,blank=False,default='null')
    is_used=models.BooleanField(default=False)