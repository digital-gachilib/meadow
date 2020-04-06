from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from books.models import Book
from books.serializers import BookSerializer

# Create your views here.
class ListBooks(APIView):
    permission_classes = (IsAuthenticated,)
    
    def get(self, request):
        books = [BookSerializer(book).data for book in Book.objects.all()]
        return Response(books)
    
    def post(self, request):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
