from django.shortcuts import render, redirect
from .models import Book
from django.views.generic.detail import DetailView
from .models import Library, UserProfile
from django.contrib.auth import views as auth_views
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.shortcuts import render
from django.contrib.auth.decorators import login_required


def list_books(request):
  books = Book.objects.all()
  context = {'books': books}
  return render(request, 'relationship_app/list_books.html', context)


class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'



# Login view (uses Django's built-in view)
class LoginView(auth_views.LoginView):
    template_name = 'relationship_app/login.html'

# Logout view (uses Django's built-in view)
class LogoutView(auth_views.LogoutView):
    template_name = 'relationship_app/logout.html'

# Registration view
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Automatically log in the user after registration
            return redirect('login')  # Redirect to login or home page
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})



# Check functions
def is_admin(user):
    return user.is_authenticated and user.userprofile.role == 'Admin'

def is_librarian(user):
    return user.is_authenticated and user.userprofile.role == 'Librarian'

def is_member(user):
    return user.is_authenticated and user.userprofile.role == 'Member'


# Views
def admin_view(request):
  if not request.user.is_authenticated:
    return redirect('login')
  if request.user.userprofile.role != UserProfile.Role.ADMIN:
    return render(request, 'relationship_app/unauthorized.html')  # Redirect to unauthorized page
  return render(request, 'relationship_app/admin_view.html')

@login_required
def librarian_view(request):
  # Similar logic as admin_view, checking for Librarian role
  if request.user.userprofile.role != UserProfile.Role.LIBRARIAN:
    return render(request, 'relationship_app/unauthorized.html')
  return render(request, 'relationship_app/librarian_view.html')

@login_required
def member_view(request):
  # Similar logic as admin_view, checking for Member role
  if request.user.userprofile.role != UserProfile.Role.MEMBER:
    return render(request, 'relationship_app/unauthorized.html')
  return render(request, 'relationship_app/member_view.html')




