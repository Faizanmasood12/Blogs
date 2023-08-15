from django.urls import path
from . import views

app_name = 'blog'
urlpatterns = [
    # making home page
    path('', views.home, name='home'),
    path('blogs/', views.blogs, name='blogs'),
    path('posts/<int:post_id>/', views.posts, name='posts'),
    path('Add blog/', views.new_blog, name='new_blog'),
    path('Add post/<int:blog_id>/', views.new_post, name='new_post'),
    path('Edit post/<int:posts_id>/', views.edit_post, name='edit_post'),
]
