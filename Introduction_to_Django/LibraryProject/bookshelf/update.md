book.title = "Nineteen Eighty-Four"
book.save()
Book.objects.get(id=book.id)

# Expected outcome
<Book: Nineteen Eighty-Four by George Orwell (1949)>