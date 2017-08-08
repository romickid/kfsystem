from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted((item, item) for item in get_all_styles())


class Admin(models.Model):
    email = models.EmailField(default='empty@empty.com', unique=True)
    nickname = models.CharField(max_length=50, default='empty', unique=True)
    password = models.CharField(max_length=128, default='empty')
    web_url = models.CharField(max_length=200, default='empty', unique=True)
    widget_url = models.CharField(max_length=200, default='empty', unique=True)
    mobile_url = models.CharField(max_length=200, default='empty', unique=True)
    communication_key = models.CharField(max_length=32, default='empty', unique=True) # TODO MD5 + salt
    vid = models.CharField(max_length=32, default='empty', unique=True)


class CustomerService(models.Model):
    email = models.EmailField(default='empty@empty.com', unique=True)
    enterprise = models.ForeignKey('Admin', on_delete=models.CASCADE)
    nickname = models.CharField(max_length=50, default='empty', unique=True)
    password = models.CharField(max_length=128, default='empty')
    is_online = models.BooleanField(default=False)
    connection_num = models.IntegerField(default=0)
    vid = models.CharField(max_length=32, default='empty', unique=True)


class ChattingLog(models.Model):
    client_id = models.CharField(max_length=100, default='empty')
    service_id = models.ForeignKey('CustomerService', on_delete=models.CASCADE)
    content = models.CharField(max_length=500, default='empty')
    is_client = models.BooleanField(default=None)
    time = models.DateTimeField(auto_now_add=True)


class SerialNumber(models.Model):
    serials = models.CharField(max_length=50, default='empty', unique=True)
    is_used = models.BooleanField(default=None)


class ImageLog(models.Model):
    client_id = models.CharField(max_length=100, default='empty')
    service_id = models.ForeignKey('CustomerService')
    image = models.ImageField(upload_to='screenshots') # TODO need to modify
    is_client = models.BooleanField(default=None)
    time = models.DateTimeField(auto_now_add=True)
