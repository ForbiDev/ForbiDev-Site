from django.http import HttpResponse, HttpRequest
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse
from django.views import View
from django.views.generic import ListView

from .forms import CommentForm
from .models import BlogPost


class BlogHomeView(ListView):
    template_name = 'blog_home.html'
    model = BlogPost
    context_object_name = 'Posts'
    paginate_by = 2

    def get_queryset(self):
        base_query = super(BlogHomeView, self).get_queryset()
        data = base_query.filter(is_show=True)
        return data


class BlogPostView(View):
    def get(self,requrst,id):
        post = BlogPost.objects.get(id=id)
        form = CommentForm
        return render(requrst,'blog_post.html',context={'post':post,'form':form})
    def post(self,request:HttpRequest,id):
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = BlogPost.objects.get(id=id)
            comment.save()
            return redirect(reverse('blog-post', args=[id]))