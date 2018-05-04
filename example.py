
from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=20)
    email = models.EmailField(max_length=254)
    password = models.CharField(max_length=20)
    permissionID = models.IntegerField(default=0)

    def __unicode__(self):
        return self.email



EMAIL_HOST = 'smtp.qq.com'
EMAIL_HOST_USER = '**********@qq.com'
EMAIL_HOST_PASSWORD = 'password'
EMAIL_PORT = 587
EMAIL_USE_TLS = True

