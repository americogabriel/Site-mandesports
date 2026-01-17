from django.shortcuts import render
from django.http.response import HttpResponse
from django.views.generic import FormView
from .models import Item,Carrinho
from .form import ItemForm

def Home(request):
    return HttpResponse('<h1> Bem Vindo a Página </h1> ')

class CreateProdutos(FormView):
    model = Item
    form_class = ItemForm
    template_name = 'catalogo/create_item.html'
    success_url = ''



