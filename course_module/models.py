from django.db import models

# Create your models here.
from account_module.models import User

Levels = (
    ('A' , 'مقدماتی'),
    ('B' , 'متوسط'),
     ('C' , 'پیشرفته'),
)

class CourseModel(models.Model):
    title = models.CharField(max_length=60, verbose_name='عنوان')
    description = models.TextField(verbose_name='توضیحات')
    image = models.ImageField(upload_to='image/courses', verbose_name='تصویر')
    teacher = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='مدرس')
    price = models.IntegerField(verbose_name='قیمت')
    level = models.CharField(verbose_name='سطح',choices=Levels,max_length=15)
    is_show = models.BooleanField(verbose_name='نمایش')
    slug = models.SlugField(verbose_name='آدرس',unique=True, default='x')
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'دوره'
        verbose_name_plural = 'دوره ها'

class CourseSeason(models.Model):
    title = models.CharField(max_length=60)
    course = models.ForeignKey(CourseModel,on_delete=models.CASCADE, verbose_name='دوره')

    def __str__(self):
        self.title

    class Meta:
        verbose_name = 'فصل'
        verbose_name_plural = 'فصل ها'

class CourseVideo(models.Model):
    title = models.CharField(max_length=60, verbose_name='عنوان')
    short_description = models.CharField(max_length=200, verbose_name='توضیح کوتاه')
    season = models.ForeignKey(CourseSeason ,on_delete=models.CASCADE, verbose_name='فصل')
    video = models.FileField(upload_to='videos/courses',verbose_name='ویدیو')

    def __str__(self):
        self.title

    class Meta:
        verbose_name = 'ویدیو'
        verbose_name_plural = 'ویدیو ها'
