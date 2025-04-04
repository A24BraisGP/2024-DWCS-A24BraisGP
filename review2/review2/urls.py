"""
URL configuration for review2 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from catalog import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.HomeView.as_view(),name='home'),
    path("product-list/", views.ProductList.as_view(), name="product-list"),
    path('create-product/',views.CreateProduct.as_view(),name="create-product"),
    path('detail/<slug:slug>/update/',views.UpdateProduct.as_view(),name='update-product'),
    path('detail/<slug:slug>/',views.DetailProduct.as_view(),name='product-detail'),
    path('detail/<slug:slug>/delete/',views.DeleteProductView.as_view(),name='delete-product'),
    path('search/',views.SearchView.as_view(),name='search'),
    
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
