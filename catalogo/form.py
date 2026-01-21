from django import forms
from .models import Item,Carrinho

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['nome','preço','descricao','imagem']
        widgets = {
            'nome': forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Nome do Item'
                }
            ),
            'preço': forms.NumberInput(
                attrs={
                    'class':'form-control',
                    'placeholder': '$Preço'
                }
            ),
            'descricao': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder':' Descreva o Produto'
                }
            ),
            'imagem': forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Digite a URL da imagem'
                }
            ),
        }