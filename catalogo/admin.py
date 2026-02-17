from django.contrib import admin
from .models import Item,Carrinho,Tipos, ItemImagem

admin.site.register(Item)
admin.site.register(Carrinho)
admin.site.register(Tipos)
admin.site.register(ItemImagem)

class ItemImagemInline(admin.TabularInline):
    model = ItemImagem
    extra = 1

class ItemAdmin(admin.ModelAdmin):
    inlines = [ItemImagemInline]
