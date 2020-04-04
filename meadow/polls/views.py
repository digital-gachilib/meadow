from book_searcher import search_by_title
from django.http import HttpResponse


def search():
    search_by_title("")
