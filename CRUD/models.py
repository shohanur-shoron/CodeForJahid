from django.db import models

class Book(models.Model):
    book_name = models.CharField(max_length=150, null=False, unique=True)
    author = models.CharField(max_length=100)
    isbn_number = models.CharField(max_length=150, null=True, blank=True)

    def __str__(self):
        return self.book_name