from django.shortcuts import render
from django.urls import reverse_lazy
from django.http.response import HttpResponse
from django.views.generic import FormView,ListView, DetailView
from .models import Item,Carrinho
from .form import ItemForm

class Home(ListView):
    model = Item
    template_name = 'catalogo/home.html'
    context_object_name = 'itens'


class ItemDetail(DetailView):
    model = Item
    template_name = 'catalogo/detail_item.html'
    context_object_name = 'Item'

class CreateProdutos(FormView):
    form_class = ItemForm
    template_name = 'catalogo/create_item.html'
    success_url = reverse_lazy('url_home')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


