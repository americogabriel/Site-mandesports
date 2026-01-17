from django.db import models


class Item(models.Model):
    nome = models.CharField(max_length= 80)
    preço = models.IntegerField()
    descricao = models.TextField()
    imagem = models.URLField()

class Carrinho(models.Model):
    item = models.ForeignKey(Item,on_delete=(models.CASCADE))
