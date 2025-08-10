from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter  # Correct import
from rest_framework import generics
from .models import Book
from .serializers import BookSerializer
from .filters import BookFilter  # Import custom filter

class BookListView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    
    # Add filter backends
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    
    # Configure filtering
    filterset_class = BookFilter
    
    # Configure search fields
    search_fields = ['title', 'author']
    
    # Configure ordering fields
    ordering_fields = ['title', 'author', 'publication_year', 'id']
    ordering = ['title']  # Default ordering
