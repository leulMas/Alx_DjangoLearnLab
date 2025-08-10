from django.db import models

class Author(models.Model):
    """
    Represents an author.
    - name: string containing the author's full name.
    The reverse relationship to Book is available at author.books (via related_name='books').
    """
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Book(models.Model):
    """
    Represents a book.
    - title: title of the book.
    - publication_year: integer year when the book was published.
    - author: foreign key to Author (many books -> one author).
    """
    title = models.CharField(max_length=255)
    publication_year = models.IntegerField()
    # related_name='books' lets us access author.books.all()
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')

    def __str__(self):
        return f"{self.title} ({self.publication_year})"
