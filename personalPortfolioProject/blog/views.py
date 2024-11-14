from django.shortcuts import render
from .models import Blog
# Create your views here.
def all_blogs(request):
    blogs = Blog.objects.all()
    if 'submit-form-1' in request.GET:
        blogs = Blog.objects.all().order_by('data')
    
    return render(request,'blog/all_blogs.html',{'blogs':blogs})