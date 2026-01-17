from django import forms
from .models import Item,Carrinho

class ItemForm(forms.ModelForm):
    class meta:
        model = Item
        fields = ['nome','preço','descricao','imagem']