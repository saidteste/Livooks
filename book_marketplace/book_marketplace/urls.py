# book_marketplace/urls.py

from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('books/', include('books.urls')),
    path('accounts/', include('django.contrib.auth.urls')),  # For authentication
    path('', views.home, name='home'),  # Home view
]
