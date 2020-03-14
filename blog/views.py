from django.shortcuts import render
from django.http import HttpResponse
from .models import Post, Tag
# Create your views here.

def post_content(request, post_id):

    post = Post.objects.get(pk=post_id)
    
    return render(request,
                  'blog/post_content.html',
                  {
                      'post': post,
                  })

def blog_list(request):
    context = {"articles":Post.objects.all()}
    return render(request, 'blog/blog_list.html', context)

def home(request):
    return render(request, 'blog/home.html')

