from django.shortcuts import render, get_object_or_404
from django.views.generic.detail import DetailView
from .models import Book, Library

# ✅ Function-based view that lists all books (as required)
def list_books(request):
    books = Book.objects.all()  # <- Required exact match
    return render(request, 'relationship_app/list_books.html', {'books': books})  # <- Required template path

# ✅ Class-based view for Library detail
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'library_detail.html'  # Still allowed
    context_object_name = 'library'
