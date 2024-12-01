from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Book, Author



class BookAPITests(APITestCase):
    def setUp(self): 
        self.author1 = Author.objects.create(name='Author One') 
        self.author2 = Author.objects.create(name='Author Two') 
        self.book1 = Book.objects.create(title='Book One', author=self.author1, publication_year=2021) 
        self.book2 = Book.objects.create(title='Book Two', author=self.author2, publication_year=2022)
        self.book_url = reverse('book-list')
    
    
    def test_create_book(self):
        data = {'title': 'New Book', 'author': 'New Author', 'publication_year': 2023}
        response = self.client.post(self.book_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 3)
    
    def test_get_books(self):
        response = self.client.get(self.book_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)
    
    def test_update_book(self):
        data = {'title': 'Updated Book', 'author': 'Updated Author'}
        response = self.client.put(reverse('book-detail', args=[self.book1.id]), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, 'Updated Book')
    
    def test_delete_book(self):
        response = self.client.delete(reverse('book-detail', args=[self.book1.id]))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 1)
    
    def test_filter_books(self):
        response = self.client.get(f"{self.book_url}?title=Book One")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], 'Book One')
    
    def test_search_books(self):
        response = self.client.get(f"{self.book_url}?search=Author Two")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['author'], 'Author Two')
    
    def test_order_books(self):
        response = self.client.get(f"{self.book_url}?ordering=publication_year")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['title'], 'Book One')
