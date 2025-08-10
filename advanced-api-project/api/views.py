from rest_framework import generics, permissions
from .models import Book
from .serializers import BookSerializer

class BookListView(generics.ListAPIView):
    """
    GET /books/
    Lists all books.
    Permission: AllowAny (public read access)
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]


class BookDetailView(generics.RetrieveAPIView):
    """
    GET /books/<int:pk>/
    Retrieves details of a single book by its ID.
    Permission: AllowAny (public read access)
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]


class BookCreateView(generics.CreateAPIView):
    """
    POST /books/create/
    Creates a new book.
    Permission: IsAuthenticated (only logged-in users)
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]


class BookUpdateView(generics.UpdateAPIView):
    """
    PUT /books/<int:pk>/update/
    Updates an existing book by ID.
    Permission: IsAuthenticated (only logged-in users)
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]


class BookDeleteView(generics.DestroyAPIView):
    """
    DELETE /books/<int:pk>/delete/
    Deletes a book by ID.
    Permission: IsAuthenticated (only logged-in users)
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]
