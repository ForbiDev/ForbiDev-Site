from django.urls import path

from .views import BlogHomeView

urlpatterns = [
    path('',BlogHomeView.as_view())
]