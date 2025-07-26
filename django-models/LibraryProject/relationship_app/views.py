from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.decorators import permission_required
from django.views.generic import ListView, DetailView
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import Book
from .models import Library
from .models import UserProfile



# Function-based view to list all books
def list_books(request):
    """
    Function-based view that lists all books stored in the database
    """
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})

# Class-based view to display library details
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['books'] = self.object.book_set.all()
        return context


# User Registration View
def register(request):
    """
    Handle user registration
    """
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})

# Role checking functions
def is_admin(user):
    """Check if user has Admin role"""
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Admin'

def is_librarian(user):
    """Check if user has Librarian role"""
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Librarian'

def is_member(user):
    """Check if user has Member role"""
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Member'

# Role-based views
@user_passes_test(is_admin)
def admin_view(request):
    """
    View accessible only to Admin users
    """
    return render(request, 'relationship_app/admin_view.html')

@user_passes_test(is_librarian)
def librarian_view(request):
    """
    View accessible only to Librarian users
    """
    return render(request, 'relationship_app/librarian_view.html')

@user_passes_test(is_member)
def member_view(request):
    """
    View accessible only to Member users
    """
    return render(request, 'relationship_app/member_view.html')

# Permission-based views for book operations
@permission_required('relationship_app.can_add_book', raise_exception=True)
def add_book(request):
    """
    View to add a new book - requires can_add_book permission
    """
    if request.method == 'POST':
        # Handle book creation here
        pass
    return render(request, 'relationship_app/add_book.html')

@permission_required('relationship_app.can_change_book', raise_exception=True)
def edit_book(request, pk):
    """
    View to edit a book - requires can_change_book permission
    """
    try:
        book = Book.objects.get(pk=pk)
        if request.method == 'POST':
            # Handle book editing here
            pass
        return render(request, 'relationship_app/edit_book.html', {'book': book})
    except Book.DoesNotExist:
        return HttpResponse("Book not found", status=404)

@permission_required('relationship_app.can_delete_book', raise_exception=True)
def delete_book(request, pk):
    """
    View to delete a book - requires can_delete_book permission
    """
    try:
        book = Book.objects.get(pk=pk)
        if request.method == 'POST':
            book.delete()
            return redirect('list_books')
        return render(request, 'relationship_app/delete_book.html', {'book': book})
    except Book.DoesNotExist:
        return HttpResponse("Book not found", status=404)