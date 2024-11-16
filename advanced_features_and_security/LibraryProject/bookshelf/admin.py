from django.contrib import admin
from .models import Book, CustomUser
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from django.contrib.auth.models import Group, Permission


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


class CustomUserAdmin(UserAdmin):
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'email', 'date_of_birth', 'profile_photo')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'date_of_birth', 'profile_photo', 'password1', 'password2'),
        }),
    )
    list_display = ('username', 'email', 'date_of_birth', 'is_staff')
    search_fields = ('username', 'email')
    ordering = ('username',)

admin.site.register(CustomUser, CustomUserAdmin)


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Book)
admin.site.register(Group)
admin.site.register(Permission)




