from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def home(request):
    return render(request, 'formularioApp/home.html')

def results(request):
    data = {'username':''}
    if request.GET.get('username'):
        data['username'] = request.GET.get('username')
        
    if request.GET.get('password'):
        data['password'] = request.GET.get('password')
        
    
    if request.GET.get('city'):
        data['city']= request.GET.get('city')
        
   
    if request.GET.get('web-server'):
        data['webServer'] = request.GET.get('web-server')
        
    
    if request.GET.get('role'):
        data['role'] = request.GET.get('role')
        
  
    if request.GET.get('sign-on1'):
        data['signOn1'] = request.GET.get('sign-on1')
     
    
    if request.GET.get('sign-on2'):
        data['signOn2'] = request.GET.get('sign-on2')    
        
    
    if request.GET.get('sign-on3'):
        data['signOn3'] = request.GET.get('sign-on3')    
        
    return render(request,'formularioApp/results.html',data)