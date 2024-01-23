from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.get_products, name='get_products'),
    path('{id}', views.product, name='CRUD_product'),
]