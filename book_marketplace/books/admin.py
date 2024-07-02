# books/admin.py

from django.contrib import admin
from .models import Book

# Définir une classe admin pour personnaliser l'affichage des modèles
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'isbn', 'price', 'seller')
    search_fields = ('title', 'author', 'isbn')
    list_filter = ('author', 'price')

# Enregistrer le modèle Book avec les options d'administration personnalisées
admin.site.register(Book, BookAdmin)
