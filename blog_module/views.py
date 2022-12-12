import sweetify
from django.http import HttpResponse, HttpRequest
from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from django.urls import reverse
from django.views import View
from django.views.generic import ListView

from .forms import CommentForm
from .models import BlogPost, PostComment


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
        post = get_object_or_404(BlogPost, id=id)
        # post = BlogPost.objects.get(id=id)
        form = CommentForm
        comments = PostComment.objects.filter(post=id)
        return render(requrst,'blog_post.html',context={'post':post,'form':form, 'comments':comments})
    def post(self,request:HttpRequest,id):
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = BlogPost.objects.get(id=id)
            comment.save()
            sweetify.success(request, 'نظر شما با موفقیت ثبت شد')
            return redirect(reverse('blog-post', args=[id]))
        sweetify.error(request,'مشکللللل')
        post = get_object_or_404(BlogPost, id=id)
        comments = PostComment.objects.filter(post=id)
        return render(request,'blog_post.html',context={'post':post,'form':form, 'comments':comments})