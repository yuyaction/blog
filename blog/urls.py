from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.home, name='home'), 
    path('blog', views.blog_list, name='blog_list'), 
    path('blog/tag', views.tag_list, name='tag_list'), 
    path('blog/<int:post_id>', views.post_content, name='post_content'),
    path('blog/tag/<str:tag_name>', views.article_with_tag, name='awt')
]
