from rest_framework import generics, permissions
from .models import Book
from .serializers import BookSerializer

class BookList(generics.ListCreateAPIView):   # Retrieve a list of all books.
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save()

class BookDetail(generics.RetrieveAPIView):     # Retrieve a single book by its ID.
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class BookCreate(generics.CreateAPIView):        # Add new book to the collection.
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save()


class BookUpdate(generics.UpdateAPIView):         # Modify an existing book.
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_update(self, serializer):
        serializer.save()

class BookDelete(generics.DestroyAPIView):        # Remove a book from the collection.
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]




    

