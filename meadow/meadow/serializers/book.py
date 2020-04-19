from rest_framework.serializers import ModelSerializer

from meadow.models import Book


class BookSerializer(ModelSerializer):
    class Meta:
        model = Book
        fields = ["id", "title", "description", "author"]
        depth = 1
