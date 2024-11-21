from django.shortcuts import render, redirect
from .models import Book
from .forms import BooktForm

def create_book(request):
    if request.method == 'POST':
        form = BooktForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BooktForm()
    return render(request, 'addBook.html', {'form': form, 'action': 'add'})

def book_list(request):
    books = Book.objects.all()
    return render(request, 'bookList.html', {'books': books})

def update_book(request, pk):
    book = Book.objects.get(pk=pk)
    if request.method == 'POST':
        form = BooktForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BooktForm(instance=book)
    return render(request, 'addBook.html', {'form': form, 'book': book, 'action': 'update'})

def delete_book(request, pk):
    try:
        book = Book.objects.get(pk=pk)
        book.delete()
        return redirect('book_list')
    except Book.DoesNotExist:
        return redirect('book_list')
