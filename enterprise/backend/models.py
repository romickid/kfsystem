from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted((item, item) for item in get_all_styles())


class Admin(models.Model):
    email = models.EmailField(default='empty@empty.com', unique=True)
    nickname = models.CharField(max_length=50, default='empty', unique=True)
    info = models.CharField(max_length=200, default='empty')
    emterprise = models.CharField(max_length=128, default='empty')
    password = models.CharField(max_length=128, default='empty')


class SecretKey(models.Model):
    secretkey = models.CharField(max_length=50, default='empty')

