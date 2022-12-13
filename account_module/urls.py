from django.urls import path
from . import views

urlpatterns = [
    path('', views.AccountView.as_view(), name='account-home'),
    path('register',views.RegisterView.as_view(), name='register'),
    path('login', views.LoginView.as_view(), name='login'),
    path('logout',views.LogoutView.as_view(), name='logout')
]