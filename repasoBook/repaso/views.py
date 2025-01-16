from django.shortcuts import render
from .models import Book
from django.shortcuts import get_object_or_404
# Create your views here.
def index(request):
  books = Book.objects.all()
  
  return render(request, 'repaso/index.html', {'books': books})

def book_detail(request,slug):
  book = get_object_or_404(Book,slug=slug)
  
  return render(request, 'repaso/detail.html',{'book':book})