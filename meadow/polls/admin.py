from django.contrib import admin

from .models import Book, BookAuthor

admin.site.register(Book)
admin.site.register(BookAuthor)
