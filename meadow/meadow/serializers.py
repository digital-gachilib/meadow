from rest_framework.serializers import ModelSerializer

from meadow.models import Book, BookAuthor
from rest_framework.fields import FileField


class BookSerializer(ModelSerializer):
    file = FileField()

    class Meta:
        model = Book
        fields = ["id", "title", "description", "author", "file"]
        depth = 1


class BookAuthorSerializer(ModelSerializer):
    class Meta:
        model = BookAuthor
        fields = ["first_name", "last_name"]
