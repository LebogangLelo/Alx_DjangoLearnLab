from rest_framework import generics, permissions
from .models import Book
from .serializers import BookSerializer


class ListView(generics.ListCreateAPIView):   # Retrieve a list of all books.
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save()

class DetailView(generics.RetrieveAPIView):     # Retrieve a single book by its ID.
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class CreateView(generics.CreateAPIView):        # Add new book to the collection.
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save()


class UpdateView(generics.UpdateAPIView):         # Modify an existing book.
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_update(self, serializer):
        serializer.save()

class DeleteView(generics.DestroyAPIView):        # Remove a book from the collection.
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]




    

