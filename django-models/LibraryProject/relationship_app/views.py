ffrom django.shortcuts import render
from django.views.generic.detail import DetailView
from .models import Book, Library  # ✅ Required exact import

# ✅ Function-based view to list all books
def list_books(request):
    books = Book.objects.all()  # ✅ Required query
    return render(request, 'relationship_app/list_books.html', {'books': books})  # ✅ Required template path

# ✅ Class-based view to show library details
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'  # ✅ Required template path
    context_object_name = 'library'
