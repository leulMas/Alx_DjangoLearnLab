from django.shortcuts import render, get_object_or_404
from django.views import View
from .models import Book, Library
from django.views.generic.detail import DetailView


def list_books(request):
    books = Book.objects.select_related('author').all()
    return render(request, 'list_books.html', {'books': books})



class LibraryDetailView(DetailView):
    model = Library
    template_name = 'library_detail.html'
    context_object_name = 'library'
