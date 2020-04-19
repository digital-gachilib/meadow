from django.db import models


class BookAuthor(models.Model):
    class Meta:
        verbose_name = "Book author"
        verbose_name_plural = "Book authors"

    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=30)
