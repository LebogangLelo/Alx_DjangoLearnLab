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

# Advanced Features and Security: Permissions and Groups in Django

This module demonstrates how to implement and manage permissions and groups to control access to various parts of a Django application. The system ensures security and tailored functionality by restricting access based on user roles and their assigned permissions.

---

## Features

- **Custom Permissions**:
  - Define specific permissions (`can_view`, `can_create`, `can_edit`, `can_delete`) for the `Document` model.
  
- **User Groups**:
  - Predefined groups: **Editors**, **Viewers**, and **Admins**.
  - Each group has a unique set of permissions assigned to control actions.

- **Access Control**:
  - Permissions enforced in both function-based and class-based views.
  - Unauthorized actions are blocked, providing enhanced security.

---

## Setup Instructions

### 1. Custom Permissions
The `Document` model includes the following permissions:
- `can_view`: Allows users to view a document.
- `can_create`: Allows users to create a new document.
- `can_edit`: Allows users to edit an existing document.
- `can_delete`: Allows users to delete a document.

These permissions are defined in the model’s `Meta` class.

### 2. Groups and Permissions
The application uses the following groups with specific permissions:

| Group      | Permissions                |
|------------|----------------------------|
| **Viewers** | `can_view`                |
| **Editors** | `can_view`, `can_create`, `can_edit` |
| **Admins**  | `can_view`, `can_create`, `can_edit`, `can_delete` |

Groups can be managed through the Django admin panel or programmatically using a script provided in `models.py`.

---

### 3. Enforcing Permissions in Views
Permissions are enforced using decorators and mixins:
- **Function-Based Views**: The `@permission_required` decorator is used.


Example:

```python
@permission_required('your_app.can_edit', raise_exception=True)
def edit_document(request, pk):
    # Logic for editing a document

# Security Measures

## Secure Settings

- `DEBUG`: Set to `False` in production.
- `SECURE_BROWSER_XSS_FILTER`, `X_FRAME_OPTIONS`, `SECURE_CONTENT_TYPE_NOSNIFF`, `CSRF_COOKIE_SECURE`, `SESSION_COOKIE_SECURE`: Configured to enhance security.

## CSRF Protection

- Ensure all forms include `{% csrf_token %}`.

## Secure Data Access

- Use Django’s ORM to avoid SQL injection.
- Validate and sanitize user inputs.

## Content Security Policy (CSP)

- Set up using `django-csp` middleware to prevent XSS attacks.

## Testing

- Manually test the application for secure handling of inputs and responses.
- Test forms and input fields for CSRF and XSS vulnerabilities.

