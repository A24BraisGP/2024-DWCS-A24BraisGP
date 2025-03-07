from django.shortcuts import render
from .forms import ProductForm
from django.views.generic import TemplateView
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy
from .models import Product, Category
# Create your views here.
class HomeView(TemplateView):
    template_name = 'catalog/home.html'
    
class ProductList(ListView):
    template_name = 'catalog/product_list.html'
    model = Product
    context_object_name = 'products'
    
class DetailProduct(DetailView):
    template_name = 'catalog/product_detail.html'
    model = Product
    context_object_name = 'product'

class CreateProduct(CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog/create_product.html'
    success_url = reverse_lazy('home')
    
class UpdateProduct(UpdateView):
    model = Product
    form_class  = ProductForm
    template_name = 'catalog/update_product.html'
    success_url = reverse_lazy('home')