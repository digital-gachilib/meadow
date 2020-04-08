from rest_framework.serializers import ModelSerializer

from meadow.models import Book, BookAuthor


class BookSerializer(ModelSerializer):
    class Meta:
        model = Book
        fields = ["id", "title", "description", "author"]
        depth = 1


class BookAuthorSerializer(ModelSerializer):
    class Meta:
        model = BookAuthor
        fields = ["first_name", "last_name"]
