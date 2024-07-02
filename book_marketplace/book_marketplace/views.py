# book_marketplace/views.py

from django.shortcuts import redirect

def home(request):
    return redirect('book_list')
