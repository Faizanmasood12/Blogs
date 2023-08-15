from django.shortcuts import render, redirect
from .models import Blogs, Posts
from .forms import BlogsForm, PostsForm
from django.contrib.auth.decorators import login_required
from django.http import Http404

# Create your views here.
def home(request):
    """creat view funcitions for home page."""
    posts = Posts.objects.order_by('-publish')

    context = {'posts': posts}
    return render(request, 'blog/Home.html', context)


@login_required()
def blogs(request):
    """Create view functoins for blogs"""
    blogs = Blogs.objects.filter(owner=request.user).order_by('-publish')

    context = {'blogs': blogs}
    return render(request, 'blog/blogs.html', context)


@login_required()
def posts(request, post_id):
    """Create view functoins for blogs"""
    blogs = Blogs.objects.get(id=post_id)
    posts = blogs.posts_set.order_by('-publish')
    check_blog_owner(request, blogs)

    context = {'blogs': blogs, 'posts': posts}
    return render(request, 'blog/posts.html', context)


@login_required()
def new_blog(request):
    """Create view functions for new_blog"""
    if request.method != 'POST':
        form = BlogsForm()
    else:
        form = BlogsForm(request.POST)
        if form.is_valid():
            new_blogs = form.save(commit=False)
            new_blogs.owner = request.user
            new_blogs.save()
            return redirect('blog:blogs')

    context = {'form': form}
    return render(request, 'blog/new_blog.html', context)


@login_required()
def new_post(request, blog_id):
    """Create view functions for new_blog"""
    blog = Blogs.objects.get(id=blog_id)
    check_blog_owner(request, blog)

    if request.method != 'POST':
        form = PostsForm()
    else:
        form = PostsForm(data=request.POST)
        if form.is_valid():
            postss = form.save(commit=False)
            postss.post = blog
            postss.save()
            return redirect('blog:posts', post_id=blog.id)

    context = {'form': form, 'blog': blog}
    return render(request, 'blog/new_post.html', context)


@login_required()
def edit_post(request, posts_id):
    """create function for edit post"""
    posts = Posts.objects.get(id=posts_id)
    blog = posts.post
    check_blog_owner(request, blog)
    if request.method != 'POST':
        form = PostsForm(instance=posts)
    else:
        form = PostsForm(instance=posts, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('blog:posts', post_id=blog.id)

    context = {'post': posts, 'blog': blog, 'form': form}
    return render(request, 'blog/edit_post.html', context)

def check_blog_owner(request, blog):
    """check user status"""
    if blog.owner != request.user:
        raise Http404
