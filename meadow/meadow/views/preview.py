from django.http import JsonResponse
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request

from meadow.utils.book_searcher import book_preview


@api_view(["GET"])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def preview(request: Request):
    if "id" not in request.query_params.keys():
        raise ValueError("No id provided!")
    book_id = request.query_params.get("id", "")
    book = book_preview(book_id)
    return JsonResponse(book)
