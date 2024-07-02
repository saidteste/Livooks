# books/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.book_list, name='book_list'),
    path('book/<int:pk>/', views.book_detail, name='book_detail'),
    path('book/new/', views.add_book, name='add_book'),
    path('book/<int:pk>/buy/', views.buy_book, name='buy_book'),
    path('signup/', views.signup, name='signup'),
]
