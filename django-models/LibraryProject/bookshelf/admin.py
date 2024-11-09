from django.contrib import admin
from .models import Book

# Register the Book model
@admin.site.register(Book)

class BookAdmin(admin.ModelAdmin):
    # Display specific fields in the list view
    list_display = ('title', 'author', 'publication_year')
    
    # Enable search by title and author fields
    search_fields = ('title', 'author')
    
    # Add filter options for publication year
    list_filter = ('publication_year',)

# Register the Book model with the customized admin interface
admin.site.register(Book, BookAdmin)


