from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.home, name='home'), 
    path('blog', views.blog_list, name='blog_list'), 
    path('blog/<int:post_id>', views.post_content, name='post_content'),
]
