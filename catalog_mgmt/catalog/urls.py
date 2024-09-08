from django.urls import path
from . import views

urlpatterns = [
    path('', views.app_home, name ='app_home'),
    path('products', views.app_products, name ='app_products'),
    path('about', views.app_about, name ='app_about'),
]