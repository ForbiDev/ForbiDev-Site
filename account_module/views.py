from django.contrib.auth import logout, login
from django.http import HttpRequest
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse
from django.utils.crypto import get_random_string
from django.views import View

from account_module.forms import RegisterForm, LoginForm
from account_module.models import User


class AccountView(View):
    def get(self, request:HttpRequest):
        return render(request, 'account_home.html', {'user':request.user})

class RegisterView(View):
    def get(self, request):
        form = RegisterForm()
        return render(request,'register.html',{'forms':form})
    def post(self,request:HttpRequest):
        form = RegisterForm(request.POST)
        if form.is_valid():
            user_name = form.cleaned_data.get('username')
            user_email = form.cleaned_data.get('email')
            user_pass = form.cleaned_data.get('password')
            user_first = form.cleaned_data.get('first_name')
            user_last = form.cleaned_data.get('last_name')
            user : bool = User.objects.filter(username__exact=user_name).exists()
            mail : bool = User.objects.filter(email__exact=user_email).exists()
            if user:
                form.add_error('username','کاربری با این نام کاربری وجود دارد')
            elif mail:
                form.add_error('email', 'کاربری با این ایمیل وجود دارد')
            else:
                New_User = User(username=user_name,is_active=True, first_name=user_first,last_name=user_last,email_active_code=get_random_string(60))
                New_User.set_password(user_pass)
                New_User.save()

                return redirect(reverse('account-home'))
        contex = {'forms':form}
        return render(request,'register.html',contex)

class LoginView(View):
    def get(self, request):
        form = LoginForm()
        contex = dict(forms=form)
        return render(request,'login.html',contex)
    def post(self,request):
        form = LoginForm(request.POST)
        if form.is_valid():
            user_mail = form.cleaned_data.get('email')
            user_pass = form.cleaned_data.get('password')
            user : User = User.objects.filter(email__exact=user_mail).first()
            if user is not None:
                pass_correct = user.check_password(user_pass)
                if pass_correct:
                    login(request,user)
                    return redirect(reverse('account-home'))
                else:
                    form.add_error('password','رمز عبور نادرست میباشد')
            else:
                form.add_error('email','کاربری با این ایمیل پیدا نشد')
            contex = {'forms':form}
            return render(request,'login.html',contex)
class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect(reverse('account-home'))
    def post(self,request):
        pass