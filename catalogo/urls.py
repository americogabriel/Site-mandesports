from django.contrib import admin
from django.urls import path
from .views import CreateProdutos,Home


urlpatterns = [
    path('home/',Home, name='url_home'),
    path('createitem/',CreateProdutos.as_view(), name= 'url_createitem'),
]