# Create Operation (create.md)
## Command:
```python
from bookshelf.models import Book
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
print(book)

# Expected outcome (Succesful creation)
<Book: 1984 by George Orwell (1949)>


# Retrieve Operation (retieve.md)
## Command:
``` python
Book.objects.get(id=book.id)

#Expected outcome
<Book: 1984 by George Orwell (1949)>


# Update Operation (update.md)
## Command:
```python
book.title = "Nineteen Eighty-Four"
book.save()
Book.objects.get(id=book.id)

#Expected outcome
<Book: Nineteen Eighty-Four by George Orwell (1949)>


# Delete Operation (delete.md)
## Command:
```python
book.delete()
Book.objects.all()

#Expected outcome
<QuerySet []>

