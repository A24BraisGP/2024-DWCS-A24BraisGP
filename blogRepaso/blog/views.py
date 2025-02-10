from django.shortcuts import render, get_object_or_404
from .models import Post,Author,Tag
from django.views.generic.base import TemplateView
from django.views.generic import ListView
from django.views.generic import DetailView

# # Create your views here.

# def home(request):
#   posts = Post.objects.all()
#   post_by_date = posts.order_by('date')[:3]
  
  
#   return render(request, 'blog/home.html',{
#     'posts':post_by_date
#   })

class MainBlogPage(TemplateView):
  template_name = 'blog/home.html'
  
  def get_context_data(self, **kwargs):
      context = super().get_context_data(**kwargs)
      context["posts"] = Post.objects.all().order_by('date')[:3] 
      return context
  

# def detail(request, slug):
#   post = get_object_or_404(Post, slug=slug)
#   return render (request, 'blog/detail.html',{'post':post})

class DetailBlog(DetailView):
  template_name = 'blog/detail.html'
  model = Post
  

# def all(request):
#   posts = Post.objects.all()
#   return render(request,'blog/all-post.html',{"posts":posts} )

class AllBlogs(ListView):
  models = Post
  template_name = 'blog/all-post.html'
  context_object_name = 'posts'
  
  def get_queryset(self):
    base_query = Post.objects.all()
    data = base_query.order_by('date')
    return data