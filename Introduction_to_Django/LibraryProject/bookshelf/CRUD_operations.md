# CRUD Operations for Book model

## CREATE
from bookshelf.models import Book  
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)  
book  
# <Book: 1984 by George Orwell (1949)>

---

## RETRIEVE
book = Book.objects.get(title="1984")  
book.title  # '1984'  
book.author  # 'George Orwell'  
book.publication_year  # 1949

---

## UPDATE
book.title = "Nineteen Eighty-Four"  
book.save()  
book  
# <Book: Nineteen Eighty-Four by George Orwell (1949)>

---

## DELETE
book.delete()  
Book.objects.all()  
# <QuerySet []>
