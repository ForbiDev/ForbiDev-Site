from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views import View


class BlogHomeView(View):
    def get(self, request):
        return HttpResponse("<h1>Hello World! from ForbiDev</h1>")