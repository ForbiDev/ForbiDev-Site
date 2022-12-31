from django.shortcuts import render

# Create your views here.
from django.views import View
from .models import CourseModel


class CourseListView(View):
    def get(self,request):
        courses = CourseModel.objects.filter(is_show=True)

        return render(request,'course_list.html',{'courses':courses})