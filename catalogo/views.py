from django.shortcuts import render,get_object_or_404, redirect
from django.contrib import messages
from django.urls import reverse_lazy, reverse
from django.http.response import HttpResponse
from django.views.generic import FormView,ListView, DetailView , CreateView , View, DeleteView , UpdateView
from .models import Item,Carrinho
from .form import ItemForm
from .permissions import SuperAdminRequiredMixin
from urllib.parse import quote

class Home(ListView):
    model = Item
    template_name = 'catalogo/home.html'
    context_object_name = 'itens'

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return Item.objects.filter(tipo=query)
        return Item.objects.all()

#----ITEM----
class ItemDetail(DetailView):
    model = Item
    template_name = 'catalogo/detail_item.html'
    context_object_name = 'Item'

class CreateItem(SuperAdminRequiredMixin, FormView):
    form_class = ItemForm
    template_name = 'catalogo/create_item.html'
    success_url = reverse_lazy('url_listaritem')

    def form_valid(self,form):
        form.save()
        return super().form_valid(form)
    
class UpdateItem(SuperAdminRequiredMixin,UpdateView):
    model = Item
    form_class = ItemForm
    template_name = 'catalogo/create_item.html'
    success_url = reverse_lazy('url_listaritem')


    def form_valid(self, form):
        messages.success(self.request,"Item atualizado com sucesso.")
        return super().form_valid(form)

class ListItem(SuperAdminRequiredMixin, ListView):
    model = Item
    template_name = 'catalogo/listar_item.html'
    context_object_name = 'Itens'

class DeletarItem(SuperAdminRequiredMixin,View):
    
    def get(self,request,pk):
        obj = get_object_or_404(Item,pk=pk)
        if obj:
            obj.delete()
            messages.success(request,"Item deletetado com sucesso")


#----CARRINHO----
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

    def get_queryset(self):
        return Carrinho.objects.filter(session_key = self.request.session.session_key)
    
    def get_context_data(self, **kwargs):
        carrinho = self.get_queryset() # Retorna a Lista com todos os itens do carrinho
        context = super().get_context_data(**kwargs)
        mensagem = "Olá! Tenho interesse nos seguintes itens:\n\n"
        numero_empresa = "558399290264"
        valor_total = 0

        for item in carrinho:
            mensagem += f"-{item.item.nome}- R${item.item.preço}\n"
            valor_total += item.item.preço

        mensagem += f"\nValor Total: R${valor_total}"
        mensagem_codificada = quote(mensagem)
        context['mensagem_url'] = f"https://wa.me/{numero_empresa}?text={mensagem_codificada}"
        context['valor_total'] = valor_total
        return context

class RemoverCarrinho(View):
    
    def get(self,request,pk):
        objeto = get_object_or_404(Carrinho,pk = pk)

        objeto.delete()
        messages.success(request,"Item removido do carrinho")

        return redirect('url_carrinho')


    

    


