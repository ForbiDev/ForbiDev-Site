from django.shortcuts import render

# Create your views here.
from django.views import View
from .models import CourseModel, CourseSeason, CourseVideo

class CoursView(View):
    def get(self, request, slug):
        course = CourseModel.objects.get(slug=slug)
        seasons = CourseSeason.objects.filter(course=course)
        contex = {
        'course' : CourseModel.objects.get(slug=slug),
        'seasons' : CourseSeason.objects.filter(course=course),
        'videos' : CourseVideo.objects.all()
        }
        return render(request, 'course_page.html', contex)
class CourseListView(View):
    def get(self,request):
        courses = CourseModel.objects.filter(is_show=True)

        return render(request,'course_list.html',{'courses':courses})