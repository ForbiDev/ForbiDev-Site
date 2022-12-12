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


class PostComment(models.Model):
    fullname = models.CharField(max_length=30, verbose_name='نام و نام خانوادگی')
    email = models.EmailField(verbose_name='ایمیل')
    content = models.TextField(verbose_name='متن کامنت')
    post = models.ForeignKey(BlogPost, on_delete=models.CASCADE, verbose_name='پست هدف')
    date = models.DateTimeField(verbose_name='تاریخ ایجاد',editable=False, auto_now_add=True)
    is_show = models.BooleanField(verbose_name='تائید',default=True)

    class Meta:
        verbose_name = 'نظر'
        verbose_name_plural = 'نظرات'

    def __str__(self):
        return f"{self.fullname} ({self.email})"