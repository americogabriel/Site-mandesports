from django.shortcuts import render,get_object_or_404, redirect
from django.contrib import messages
from django.urls import reverse_lazy, reverse
from django.http.response import HttpResponse
from django.views.generic import FormView,ListView, DetailView , CreateView , View, DeleteView
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
        if not request.session.session_key:
            request.session.create()
        session_key = request.session.session_key

        item = get_object_or_404(Item,pk = pk)
        objeto,create = Carrinho.objects.get_or_create(session_key = session_key, item=item) ## Se o objeto foi criado agora o create retorna True, caso contrario retorna False

        if not create:
            messages.warning(request,"Este Item já está em seu carrinho")
        else:
            messages.success(request,"Item adicionado ao carrinho com sucesso")

        return redirect('url_item_detail', pk = pk)
    
class ListarCarrinho(ListView):
    model = Carrinho
    template_name = 'catalogo/carrinho.html'
    context_object_name = 'Carrinhos'

class RemoverCarrinho(View):
    
    def get(self,request,pk):
        objeto = get_object_or_404(Carrinho,pk = pk)

        objeto.delete()
        messages.success(request,"Item removido do carrinho")

        return redirect('url_carrinho')


    

    


