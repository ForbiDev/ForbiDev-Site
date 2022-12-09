from django.db import models

# Create your models here.
from account_module.models import User


class BlogPost(models.Model):
    title = models.CharField(max_length=60, verbose_name='عنوان')
    short_description = models.CharField(max_length=150, verbose_name='توضیحات کوتاه')
    content = models.TextField(verbose_name='متن مقاله')
    is_show = models.BooleanField(default=True, verbose_name='نمایش')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='نویسنده')

    class Meta:
        verbose_name = 'مقاله'
        verbose_name_plural = 'مقالات'

    def __str__(self):
        return self.title