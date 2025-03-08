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
  




class AllBlogs(ListView):
  models = Post
  template_name = 'blog/all-post.html'
  context_object_name = 'posts'
  
  def get_queryset(self):
    base_query = Post.objects.all()
    data = base_query.order_by('date')
    return data
  
class DetailBlog(View):

  def get(self, request,slug):
    post = Post.objects.get(slug=slug)
    
    context = {
      'post':post,
      'comment_form' : CommentForm(),
      'comments': Comment.objects.filter(post=post).order_by('-id'),
      'saved_for_later': self.is_stored_post(request,post.id),
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
  
  def is_stored_post(self, request, post_id):
    stored_posts = request.session.get('stored_posts')
    is_saved_for_later = False
    if stored_posts is None:
      is_saved_for_later = False
    else: 
      is_saved_for_later = post_id in stored_posts
    return is_saved_for_later
  
  
# View que traballa coas sesións
class ReadLaterView(View):  
  def get(self, request):
    stored_posts = request.session.get('stored_posts')
    context = {}
    #Colle da BD os posts tales que o ID estean na lista de ids gardados na sesión
    if stored_posts is None or len(stored_posts) == 0:
      context['posts'] = []
      context['has_posts'] = False
    else:
      posts = Post.objects.filter(id__in=stored_posts)
      context['posts'] = posts
      context['has_posts'] = True

    return render(request,'blog/stored-posts.html',context)
    
  def post(self,request):
    stored_posts = request.session.get('stored_posts')
    if stored_posts is None:
      stored_posts = []
    post_id = int(request.POST['post_id'])
    if post_id not in stored_posts:
      stored_posts.append(post_id)
    else:
      stored_posts.remove(post_id)
    request.session['stored_posts'] = stored_posts
    
    return HttpResponseRedirect('/')