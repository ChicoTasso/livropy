from django.contrib import admin
from .models import Autor, Livro
# Register your models here.

class LivroInline(admin.TabularInline):
    model = Livro

@admin.register(Autor)
class AutorAdmin(admin.ModelAdmin):
    list_display = ["nome", "email"]
    search_fields = ["nome"]
    inlines = [ LivroInline ]

@admin.register(Livro)
class LivroAdmin(admin.ModelAdmin):
    list_display = ["titulo", "ano", "escritor"]
    autocomplete_fields = ["escritor"]