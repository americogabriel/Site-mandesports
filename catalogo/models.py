from django.db import models

class Tipos(models.Model):
    tipo_mercadoria = models.CharField(max_length= 30)

    class Meta:
        verbose_name_plural = "Tipos"
    
    def __str__(self):
        return self.tipo_mercadoria

class Item(models.Model):
    nome = models.CharField(max_length= 80)
    tipo = models.ForeignKey(Tipos,on_delete=(models.CASCADE))
    preço = models.DecimalField( max_digits= 10,decimal_places= 2)
    descricao = models.TextField()

    class Meta:
        verbose_name_plural = "Itens"
        
    def __str__(self):
        return self.nome

class ItemImagem(models.Model):
    item = models.ForeignKey(Item,on_delete=(models.CASCADE),related_name='imagens')
    imagem = models.ImageField(upload_to='itens/')

class Carrinho(models.Model):
    session_key = models.CharField(max_length=40)
    item = models.ForeignKey(Item,on_delete=(models.CASCADE))

    class Meta:
        verbose_name_plural = "Carrinho"

    def __str__(self):
        return self.item.nome
