from rest_framework.serializers import ModelSerializer

from meadow.models import BookAuthor


class BookAuthorSerializer(ModelSerializer):
    class Meta:
        model = BookAuthor
        fields = ["first_name", "last_name"]
