from django.db import models


class Item(models.Model):
    nome = models.CharField(max_length= 80)
    preço = models.IntegerField()
    descricao = models.TextField()
    imagem = models.URLField()

    class Meta:
        verbose_name_plural = "Itens"
        
    def __str__(self):
        return self.nome

class Carrinho(models.Model):
    session_key = models.CharField()
    item = models.ForeignKey(Item,on_delete=(models.CASCADE))

    class Meta:
        verbose_name_plural = "Carrinho"

    def __str__(self):
        return self.item.nome
