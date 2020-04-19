from django.contrib.auth.models import User
from django.db import models


class BookAuthor(models.Model):
    class Meta:
        verbose_name = "Book author"
        verbose_name_plural = "Book authors"

    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=30)


class Book(models.Model):
    class Meta:
        verbose_name = "Book"
        verbose_name_plural = "Books"

    title = models.CharField(max_length=200)
    isbn_10 = models.IntegerField
    isbn_13 = models.CharField(max_length=15)
    description = models.TextField()
    author = models.ForeignKey(BookAuthor, related_name="books", on_delete=models.CASCADE)
