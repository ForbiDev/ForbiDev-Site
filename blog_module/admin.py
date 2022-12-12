from django.contrib import admin
from . import models

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'is_show']
    list_editable = ['is_show']


class CommentAdmin(admin.ModelAdmin):
    list_display = ['fullname', 'email','date','is_show']
    list_editable = ['is_show']

admin.site.register(models.BlogPost, PostAdmin)
admin.site.register(models.PostComment, CommentAdmin)
