from django import forms
from .models import Book

class BooktForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['book_name', 'author', 'isbn_number']