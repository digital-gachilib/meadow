from rest_framework.serializers import ModelSerializer

from meadow.models import Book, BookAuthor


class BookSerializer(ModelSerializer):
    # todo: add inner serializer for author field
    # i.e. instead of
    # { "id": 2, "title": "ad", "description": "dsfd"}
    # we should return
    # { "id": 2, "title": "ad", "description": "dsfd",
    #   "author": { "first_name": "SD", "last_name": "DSFDS" }
    # }
    # might be useful in solving this task:
    # https://www.django-rest-framework.org/tutorial/5-relationships-and-hyperlinked-apis/
    # I didn't manage to get thought it yet

    class Meta:
        model = Book
        fields = ["id", "title", "description"]


class BookAuthorSerializer(ModelSerializer):
    class Meta:
        model = BookAuthor
        fields = ["first_name", "last_name"]
