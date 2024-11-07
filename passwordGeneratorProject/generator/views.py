from django.shortcuts import render
from django.http import HttpResponse
import random
# Create your views here.
def home(request):
    return render(request,'generator/home.html')
def about(request):
    return render(request,"generator/about.html")
def password(request):
    
    characters = list('abcdefghijklmnpqrstuvwxyz')
    
    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWYXZ'))
    if request.GET.get('special'):
        characters.extend(list('_-$%&/()·"!=ç'))
    if request.GET.get('numbers'):  
        characters.extend(list('0123456789'))
    
    
    
    
    length = int(request.GET.get('length',12))
    
    password = ' '
    for item in range(length):
        password += random.choice(characters)
    
    return render(request,'generator/password.html',{'password':password})
def eggs(request):
    return HttpResponse("Eggs are so yummy")