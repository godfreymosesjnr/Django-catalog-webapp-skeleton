from django.shortcuts import render
from django.http import HttpResponse

def app_home(request):
    return render(request, 'catalog/home.html')

def app_products(request):
    return render(request, 'catalog/products.html')

def app_about(request):
    return render(request, 'catalog/about.html')

