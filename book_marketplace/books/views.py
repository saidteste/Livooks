from django.shortcuts import render, get_object_or_404, redirect
from .models import Book, Transaction
from .forms import BookForm
from django.contrib.auth.decorators import login_required
# ---------------

from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from .forms import SignUpForm


def book_list(request):
    books = Book.objects.all()
    return render(request, 'books/book_list.html', {'books': books})

@login_required
def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, 'books/book_detail.html', {'book': book})

@login_required
def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            book = form.save(commit=False)
            book.seller = request.user
            book.save()
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'books/book_form.html', {'form': form})

@login_required
def buy_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    transaction = Transaction(book=book, buyer=request.user)
    transaction.save()
    book.delete()  # Remove the book from the marketplace after purchase
    return redirect('book_list')


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('book_list')
    else:
        form = SignUpForm()
    return render(request, 'books/signup.html', {'form': form})
