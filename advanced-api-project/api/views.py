# api/views.py
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework import generics, permissions
from .models import Book
from .serializers import BookSerializer
from rest_framework import filters

# List all books (read-only for unauthenticated users)
class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['title', 'author']
    search_fields = ['title', 'author']
    permission_classes = [permissions.AllowAny]  # anyone can read
    permission_classes = [IsAuthenticatedOrReadOnly]

# Retrieve a single book by ID (read-only for unauthenticated users)
class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]

# Create a new book (authenticated users only)
class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

  def perform_create(self, serializer):
        # For example, you can add extra data here before saving
        serializer.save()
        
# Update an existing book (authenticated users only)
class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]
    
     def perform_update(self, serializer):
        # Add extra logic if needed before updating
        serializer.save()

# Delete a book (authenticated users only)
class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]
