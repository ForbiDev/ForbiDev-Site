from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class User(AbstractUser):
    email_active_code = models.CharField(max_length=100, verbose_name='کد فعالسازی')
    profile = models.ImageField(upload_to='images/avatars', null=True, blank=True, verbose_name='پروفایل کاربر')
    bio = models.TextField(verbose_name='بیوگرافی کاربر')

    class Meta:
        verbose_name='کاربر'
        verbose_name_plural = 'کاربران'

    def __str__(self):
        return self.get_full_name()