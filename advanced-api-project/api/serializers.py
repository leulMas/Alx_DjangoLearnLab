# api/serializers.py
from rest_framework import serializers
from .models import Author, Book
from datetime import date

class BookSerializer(serializers.ModelSerializer):
    """
    Serializes Book model (all fields).
    Includes custom validation to ensure publication_year is not in the future.
    """
    class Meta:
        model = Book
        fields = ['id', 'title', 'publication_year', 'author']
        read_only_fields = ['id']

    def validate_publication_year(self, value):
        """
        Field-level validation: ensures the publication year is not in the future.
        Raises a serializers.ValidationError if invalid.
        """
        current_year = date.today().year
        if value > current_year:
            raise serializers.ValidationError("publication_year cannot be in the future.")
        return value


class AuthorSerializer(serializers.ModelSerializer):
    """
    Serializes Author model.
    - name: author's name
    - books: nested list of books for this author using BookSerializer

    Note:
    - books is read-only here (we're using BookSerializer with read_only=True).
      If you want to create nested books when creating/updating authors, you'd implement
      custom create/update methods to accept nested data.
    """
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['id', 'name', 'books']
        read_only_fields = ['id']

