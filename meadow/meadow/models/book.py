from django.db import models

from meadow.models.book_author import BookAuthor


class Book(models.Model):
    class Meta:
        verbose_name = "Book"
        verbose_name_plural = "Books"

    title = models.CharField(max_length=200)

    # todo: unique=Tru
    isbn_10 = models.CharField(max_length=10)

    # todo: unique=Tru
    isbn_13 = models.CharField(max_length=13)
    description = models.TextField()
    author = models.ForeignKey(BookAuthor, related_name="books", on_delete=models.CASCADE)

    # todo: blank=False
    download_link = models.CharField(max_length=200, default="")
    is_approved = models.BooleanField(default=False)
