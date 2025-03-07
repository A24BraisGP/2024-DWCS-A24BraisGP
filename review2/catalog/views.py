from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic import ListView
from django.views.generic.detail import DetailView

from .models import Product, Category
# Create your views here.
class HomeView(TemplateView):
    template_name = 'catalog/home.html'
    
class ProductList(ListView):
    template_name = 'catalog/product_list.html'
    model = Product
    context_object_name = 'products'
    
class DetailProduct(DetailView):
    pass