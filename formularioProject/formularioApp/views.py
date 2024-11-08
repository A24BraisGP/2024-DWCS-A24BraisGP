from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    username = ''
    if request.GET.get('username'):
        username = request.GET.get('username')
        
    password = ''
    if request.GET.get('password'):
        password = request.GET.get('password')
        
    city = ''
    if request.GET.get('city'):
        city = request.GET.get('city')
        
    webServer = ''
    if request.GET.get('web-server'):
        webServer = request.GET.get('web-server')
        
    role = ''
    if request.GET.get('role'):
        role = request.GET.get('web-server')
        
    signOn = ''
    if request.GET.get('sign-on'):
        signOn = request.GET.get('sign-on')


    return render(request, 'formularioApp/home.html',{'username':username, 'password':password,'city':city,'web-server':webServer,'role':role,'sign-on':signOn})

# Create your views here.
