from django import forms
from .models import Book
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'isbn', 'price']


class SignUpForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
