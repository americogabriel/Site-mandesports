from django.shortcuts import render,get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.http.response import HttpResponse
from django.views.generic import FormView,ListView, DetailView , CreateView , View
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

class CreateCarrinho(View):
    def post(self,request,pk):
        item = get_object_or_404(Item,pk = pk)
        Carrinho.objects.create(item=item)

        return redirect('url_item_detail', pk = pk)
    
class ListarCarrinho(ListView):
    model = Carrinho
    template_name = 'catalogo/carrinho.html'
    context_object_name = 'Carrinhos'
    

    


