from django.http import JsonResponse
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated

from meadow.serializers import BookSerializer
from meadow.utils.book_searcher import search_by_title


@api_view(["GET"])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def search(request, title):
    books = search_by_title(title)
    serializer = BookSerializer(books, many=True)

    return JsonResponse(serializer.data, safe=False)
