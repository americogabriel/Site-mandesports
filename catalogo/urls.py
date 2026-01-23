from django.contrib import admin
from django.urls import path
from .views import CreateProdutos,Home, ItemDetail, CreateCarrinho , ListarCarrinho


urlpatterns = [
    path('',Home.as_view(), name='url_home'),
    path('createitem/',CreateProdutos.as_view(), name= 'url_createitem'),
    path('detail/<int:pk>/',ItemDetail.as_view(), name='url_item_detail'),
    path('addcarrinho/<int:pk>',CreateCarrinho.as_view(), name='url_addcarrinho'),
    path('carrinho/',ListarCarrinho.as_view(),name="url_carrinho")
]