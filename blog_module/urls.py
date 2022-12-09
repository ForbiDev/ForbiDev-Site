from django.urls import path

from .views import BlogHomeView,BlogPostView

urlpatterns = [
    path('',BlogHomeView.as_view(), name='blog-home'),
    path('<id>',BlogPostView.as_view(),name='blog-post')
]