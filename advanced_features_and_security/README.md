settings.py: Configuration for the Django project.
urls.py: The URL declarations for the project; a “table of contents” of your Django-powered site.
manage.py: A command-line utility that lets you interact with this Django project

# Django Permissions and Groups Setup

## Custom Permissions

# In models.py`:

class Book(models.Model):
    ...
    class Meta:
        permissions = [
            ("can_view", "Can view book"),
            ("can_create", "Can create book"),
            ("can_edit", "Can edit book"),
            ("can_delete", "Can delete book"),
        ]

groups_permissions = {
    "Editors": ["can_edit", "can_create"],
    "Viewers": ["can_view"],
    "Admins": ["can_view", "can_create", "can_edit", "can_delete"],
}