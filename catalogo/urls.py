from django.contrib import admin
from django.urls import path
from .views import CreateProdutos,Home, ItemDetail


urlpatterns = [
    path('',Home.as_view(), name='url_home'),
    path('createitem/',CreateProdutos.as_view(), name= 'url_createitem'),
    path('detail/<int:pk>/',ItemDetail.as_view(), name='url_item_detail')
]