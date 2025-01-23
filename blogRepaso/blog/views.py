from django.shortcuts import render, get_object_or_404
from .models import Post,Author,Tag

# Create your views here.
def home(request):
  posts = Post.objects.all()
  post_by_date = posts.order_by('date')[:3]
  
  
  return render(request, 'blog/home.html',{
    'posts':post_by_date
  })

def detail(request, slug):
  post = get_object_or_404(Post, slug=slug)
  return render (request, 'blog/detail.html',{'post':post})

def all(request):
  posts = Post.objects.all()
  return render(request,'blog/all-post.html',{"posts":posts} )