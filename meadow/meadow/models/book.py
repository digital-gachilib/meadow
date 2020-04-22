from django.db import models

from meadow.models.book_author import BookAuthor


class Book(models.Model):
    class Meta:
        verbose_name = "Book"
        verbose_name_plural = "Books"

    title = models.CharField(max_length=200)
    isbn_10 = models.IntegerField(unique=True)
    isbn_13 = models.CharField(max_length=15, unique=True)
    description = models.TextField()
    author = models.ForeignKey(BookAuthor, related_name="books", on_delete=models.CASCADE)
    download_link = models.CharField(max_length=200, default="")
