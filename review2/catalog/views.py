from django.shortcuts import render
from .forms import ProductForm
from django.views import View
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy
from .models import Product, Category
from django.http import HttpResponseRedirect
# Create your views here.
class HomeView(View):    
    def post(self,request):
        favourites = request.session.get('favourites')
        if favourites is None or len(favourites) == 0:
            favourites = []
        product_id = int(request.POST['product_id'])
        if product_id not in favourites:
            favourites.append(product_id)
        else:
            favourites.remove(product_id)
        request.session['favourites'] = favourites
        products = Product.objects.filter(id__in=favourites)
        return HttpResponseRedirect('/')
    
    def get(self,request):
        favourites = request.session.get('favourites')
        context = {}
        if favourites is None or len(favourites) == 0:
            context['products'] = []
            context['favs'] = False
        else: 
            products = Product.objects.filter(id__in=favourites)
            context['products'] = products
            context['favs'] = True
        return render(request, 'catalog/home.html',context)
class ProductList(ListView):
    template_name = 'catalog/product_list.html'
    model = Product
    context_object_name = 'products'
    
    
    
    
class DetailProduct(DetailView):
    template_name = 'catalog/product_detail.html'
    model = Product
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        product = context['product']
        favourites = self.request.session.get('favourites')
        is_in_fav = False
        if favourites is None:
            is_in_fav = False
        else: 
            is_in_fav = product.id in favourites
        context['is_fav'] = is_in_fav
        return context
            
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
    
    
class DeleteProductView(DeleteView):
    model = Product
    template_name = 'catalog/delete_product.html'
    success_url = reverse_lazy('home')
    
class SearchView(ListView):
     template_name = 'catalog/search.html'
     model = Product
     context_object_name = 'products'
     
     def get_queryset(self,**kwargs):
         products = Product.objects.all()
         product_filter = self.request.GET.get('filter')
         if product_filter:
             products = self.filter_products(product_filter)
         return products
     
     def filter_products(self, product_filter):
            order_by_mapping = {
                'name': 'name',
                'price': 'price',
                'higherPrice': '-price'
            }
            favourites = self.request.session.get('favourites')
            print(favourites)
            if product_filter == 'favourites':
                if favourites is None: 
                    products = Product.objects.all()
                else:
                    products = Product.objects.filter(id__in=favourites)
            elif product_filter not in order_by_mapping:
                category = Category.objects.get(name=product_filter)
                products = category.products.all()
            
            elif product_filter in order_by_mapping:
                products = Product.objects.all().order_by(order_by_mapping[product_filter])
               
            return products



                      