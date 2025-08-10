from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from django.contrib.auth.models import User
from .models import Author, Book

class BookAPITestCase(APITestCase):
    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(username='testuser', password='testpass')
        # Create an author
        self.author = Author.objects.create(name='Author Test')
        # Create a book
        self.book = Book.objects.create(title='Initial Book', publication_year=2020, author=self.author)
        # APIClient instance
        self.client = APIClient()

    def test_list_books(self):
        url = reverse('book-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)

    def test_retrieve_book(self):
        url = reverse('book-detail', kwargs={'pk': self.book.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], self.book.title)

    def test_create_book_unauthenticated(self):
        url = reverse('book-create')
        data = {
            'title': 'New Book',
            'publication_year': 2021,
            'author': self.author.id
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_create_book_authenticated(self):
        self.client.login(username='testuser', password='testpass')
        url = reverse('book-create')
        data = {
            'title': 'New Book Auth',
            'publication_year': 2021,
            'author': self.author.id
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['title'], 'New Book Auth')

    def test_update_book(self):
        self.client.login(username='testuser', password='testpass')
        url = reverse('book-update', kwargs={'pk': self.book.pk})
        data = {
            'title': 'Updated Book Title',
            'publication_year': 2022,
            'author': self.author.id
        }
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book.refresh_from_db()
        self.assertEqual(self.book.title, 'Updated Book Title')

    def test_delete_book(self):
        self.client.login(username='testuser', password='testpass')
        url = reverse('book-delete', kwargs={'pk': self.book.pk})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Book.objects.filter(pk=self.book.pk).exists())

    def test_filter_books_by_title(self):
        url = reverse('book-list') + '?search=Initial'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(any('Initial' in book['title'] for book in response.data))

    def test_order_books_by_publication_year(self):
        # Create another book with different year
        Book.objects.create(title='Another Book', publication_year=2019, author=self.author)
        url = reverse('book-list') + '?ordering=publication_year'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        years = [book['publication_year'] for book in response.data]
        self.assertEqual(years, sorted(years))

    def test_permissions_for_unauthenticated_user(self):
        url_update = reverse('book-update', kwargs={'pk': self.book.pk})
        url_delete = reverse('book-delete', kwargs={'pk': self.book.pk})
        response_update = self.client.put(url_update, {'title': 'Fail Update', 'publication_year': 2022, 'author': self.author.id})
        response_delete = self.client.delete(url_delete)
        self.assertEqual(response_update.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(response_delete.status_code, status.HTTP_401_UNAUTHORIZED)
