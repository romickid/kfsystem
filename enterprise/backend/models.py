from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted((item, item) for item in get_all_styles())


class Customer(models.Model):
    email = models.EmailField(default='empty@empty.com', unique=True)
    nickname = models.CharField(max_length=50, default='empty', unique=True)
    password = models.CharField(max_length=128, default='empty')
    telephone = models.CharField(max_length=20, default='empty')
    location = models.CharField(max_length=100, default='empty')
    description = models.CharField(max_length=200, default='empty')

class CommunicationKey(models.Model):
    key = models.CharField(max_length=32, default='empty')
    myid = models.IntegerField(default=0)
