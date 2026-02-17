from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import Home, CreateItem, UpdateItem, ItemDetail, CreateCarrinho, ListarCarrinho, RemoverCarrinho, ListItem, DeletarItem


urlpatterns = [
    path('',Home.as_view(), name='url_home'),
    path('createitem/',CreateItem.as_view(), name='url_createitem'),
    path('updateitem/<int:pk>',UpdateItem.as_view(), name ='url_updateitem'),
    path('listaritem/',ListItem.as_view(), name='url_listaritem'),
    path('deletaritem/<int:pk>',DeletarItem.as_view(), name='url_deletaritem'),
    path('detail/<int:pk>/',ItemDetail.as_view(), name='url_item_detail'),
    path('addcarrinho/<int:pk>',CreateCarrinho.as_view(), name='url_addcarrinho'),
    path('removercarrinho/<int:pk>',RemoverCarrinho.as_view(), name = "url_removercarrinho"),
    path('carrinho/',ListarCarrinho.as_view(), name="url_carrinho")
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )