from django.contrib import admin

# Register your models here.
from .models import CourseModel


class CourseAdmin(admin.ModelAdmin):
    list_display = ['title','teacher','price','level','is_show']
    list_editable = ['is_show']


admin.site.register(CourseModel, CourseAdmin)