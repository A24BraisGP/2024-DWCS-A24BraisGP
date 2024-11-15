from django.shortcuts import render
from .models import Blog
# Create your views here.
def all_blogs(request):
    blogs = Blog.objects.all()
<<<<<<< HEAD
=======
    if 'submit-form-1' in request.GET:
        blogs = Blog.objects.all().order_by('data')
>>>>>>> 0d3b9debf3dfa4c7295338d8fec76579e0c8a2f9
    
    return render(request,'blog/all_blogs.html',{'blogs':blogs})