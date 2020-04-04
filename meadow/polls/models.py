from django.db import models


class BookAuthor(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=30)


class Book(models.Model):
    title = models.CharField(max_length=200)
    isbn_10 = models.IntegerField
    isbn_13 = models.CharField(max_length=15)
    description = models.CharField(max_length=10000)
    author = models.ForeignKey(BookAuthor, on_delete=models.CASCADE)
