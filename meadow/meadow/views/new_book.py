from django.http import JsonResponse
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request

from meadow.utils.new_book import create_new_book


@api_view(["GET"])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def create_new_book(request: Request):
    if "first_name" not in request.query_params.keys():
        raise ValueError("No first_name provided!")
    if "last_name" not in request.query_params.keys():
        raise ValueError("No last_name provided!")
    if "link" not in request.query_params.keys():
        raise ValueError("No link provided!")
    if "title" not in request.query_params.keys():
        raise ValueError("No title provided!")
    if "description" not in request.query_params.keys():
        raise ValueError("No description provided!")
    book_link = request.query_params.get("link", "")
    book_title = request.query_params.get("title", "")
    book_description = request.query_params.get("description", "")
    author_last_name = request.query_params.get("last_name", "")
    author_first_name = request.query_params.get("first_name", "")
    book = create_new_book(book_title, book_link, book_description, author_first_name, author_last_name)
    return JsonResponse(book)
