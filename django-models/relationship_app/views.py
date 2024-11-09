from django.shortcuts import render, redirect
from .models import Book
from django.views.generic.detail import DetailView
from .models import Library
from django.contrib.auth import views as auth_views
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login


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



