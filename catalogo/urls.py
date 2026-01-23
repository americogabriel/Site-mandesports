from django.contrib import admin
from django.urls import path
from .views import Home, CreateProdutos, ItemDetail, CreateCarrinho, ListarCarrinho, RemoverCarrinho


urlpatterns = [
    path('',Home.as_view(), name='url_home'),
    path('createitem/',CreateProdutos.as_view(), name= 'url_createitem'),
    path('detail/<int:pk>/',ItemDetail.as_view(), name='url_item_detail'),
    path('addcarrinho/<int:pk>',CreateCarrinho.as_view(), name='url_addcarrinho'),
    path('removercarrinho/<int:pk>',RemoverCarrinho.as_view(), name = "url_removercarrinho"),
    path('carrinho/',ListarCarrinho.as_view(),name="url_carrinho")
]