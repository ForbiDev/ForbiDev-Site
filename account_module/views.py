from django.shortcuts import render

# Create your views here.
from django.views import View

class AccountView(View):
    def get(self, request):
        return render(request, 'account_home.html')

class RegisterView(View):
    def get(self, request):
        pass
    def post(self,request):
        pass

class LoginView(View):
    def get(self, request):
        pass
    def post(self,request):
        pass

class LogoutView(View):
    def get(self, request):
        pass
    def post(self,request):
        pass