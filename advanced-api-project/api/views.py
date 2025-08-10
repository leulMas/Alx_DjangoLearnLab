from rest_framework import viewsets
from .models import Author, Book
from .serializers import AuthorSerializer, BookSerializer

class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    
class BookListView(generics.ListAPIView):
    """
    GET /books/
    Retrieves a list of all books.
    Accessible to both authenticated and unauthenticated users.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]  # read-only for anyone


# -----------------------------
# Retrieve one book by ID
# -----------------------------
class BookDetailView(generics.RetrieveAPIView):
    """
    GET /books/<id>/
    Retrieves details of a single book by ID.
    Accessible to both authenticated and unauthenticated users.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]


# -----------------------------
# Create a new book
# -----------------------------
class BookCreateView(generics.CreateAPIView):
    """
    POST /books/create/
    Creates a new book.
    Accessible only to authenticated users.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]  # only logged-in users

    def perform_create(self, serializer):
        """
        Optionally modify data before saving.
        Here we just save normally, but you could add user association, logging, etc.
        """
        serializer.save()


# -----------------------------
# Update an existing book
# -----------------------------
class BookUpdateView(generics.UpdateAPIView):
    """
    PUT/PATCH /books/<id>/update/
    Updates an existing book.
    Accessible only to authenticated users.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]


# -----------------------------
# Delete a book
# -----------------------------
class BookDeleteView(generics.DestroyAPIView):
    """
    DELETE /books/<id>/delete/
    Deletes a book by ID.
    Accessible only to authenticated users.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]
Step 2 — URL patterns
Create a new file api/urls.py (if it doesn’t exist yet):

python
Copy
Edit
# api/urls.py
from django.urls import path
from .views import (
    BookListView,
    BookDetailView,
    BookCreateView,
    BookUpdateView,
    BookDeleteView,
)

urlpatterns = [
    path('books/', BookListView.as_view(), name='book-list'),
    path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail'),
    path('books/create/', BookCreateView.as_view(), name='book-create'),
    path('books/<int:pk>/update/', BookUpdateView.as_view(), name='book-update'),
    path('books/<int:pk>/delete/', BookDeleteView.as_view(), name='book-delete'),
]
