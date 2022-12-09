from django.contrib import admin
from .models import *
from account_module import models
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'is_show']
    list_editable = ['is_show']

admin.site.register(BlogPost, PostAdmin)
admin.site.register(models.User)