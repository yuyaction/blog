from django.shortcuts import render
from django.http import HttpResponse
from .models import Post, Tag
# Create your views here.

def post_content(request, post_id):
    context = {"post":Post.objects.get(pk=post_id)}
    return render(request, 'blog/post_content.html', context)

def blog_list(request):
    context = {"articles":Post.objects.filter(publish=True).order_by('-published_time')}
    return render(request, 'blog/blog_list.html', context)

def tag_list(request):
    context = {"tags":Tag.objects.all()}
    return render(request, 'blog/tag_list.html', context)

def home(request):
    return render(request, 'blog/home.html')

def article_with_tag(request,tag_name):
    t = Tag.objects.get(name=tag_name)
    context ={"awt":Post.objects.filter(tags=t), "selected_tag":t}
    return render(request, 'blog/awt.html', context)

