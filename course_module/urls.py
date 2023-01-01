from django.urls import path
from .views import *
urlpatterns = [
    path('', CourseListView.as_view(), name='course-list'),
    path('<slug:slug>', CoursView.as_view(), name='course-page')
]