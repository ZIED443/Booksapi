from rest_framework import serializers
from apps.bookstore.models import Book, Author

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ["id", "name", "birthday"]


class BookSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(read_only=True)
    author_id = serializers.PrimaryKeyRelatedField(
        queryset=Author.objects.all(), source="author", write_only=True
    )
    available_copies = serializers.IntegerField(read_only=True)

    class Meta:
        model = Book
        fields = ["id", "name", "author", "author_id", "date_release", "total_copies", "available_copies"]

    def validate_total_copies(self, value):
        if value < 1:
            raise serializers.ValidationError("There must be at least 1 copy")
        return value
