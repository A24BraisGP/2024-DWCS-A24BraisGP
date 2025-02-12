from django.shortcuts import render, get_object_or_404
from .models import Post,Comment
from .forms import CommentForm
from django.views.generic.base import TemplateView
from django.views.generic import ListView
from django.views import View
from django.http import HttpResponseRedirect
from django.urls import reverse


class MainBlogPage(TemplateView):
  template_name = 'blog/home.html'
  
  def get_context_data(self, **kwargs):
      context = super().get_context_data(**kwargs)
      context["posts"] = Post.objects.all().order_by('date')[:3] 
      return context
  



class DetailBlog(View):

  def get(self, request,slug):
    post = Post.objects.get(slug=slug)
    context = {
      'post':post,
      'comment_form' : CommentForm(),
      'comments': Comment.objects.filter(post=post).order_by('-id')
    }
    return render(request, 'blog/detail.html',context)
    
  def post(self,request,slug):
    comment_form = CommentForm(request.POST)
    post = Post.objects.get(slug=slug)
    if comment_form.is_valid():
      comment = comment_form.save(commit=False)
      comment.post = post
      comment.save()
      return HttpResponseRedirect(reverse('post-detail',args=[slug]))

    context = {
      'post':post,
      'comment_form' : CommentForm(),      
    }
    return render(request, 'blog/detail.html',context)

class AllBlogs(ListView):
  models = Post
  template_name = 'blog/all-post.html'
  context_object_name = 'posts'
  
  def get_queryset(self):
    base_query = Post.objects.all()
    data = base_query.order_by('date')
    return data