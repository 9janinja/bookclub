from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from books.models import Book
from .forms import BookForm

# Create your views here.


@login_required
def book_list(request):
    books = Book.objects.all()
    return render(request, 'books/book_list.html', {'books': books})    

@login_required
def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            book = form.save(commit=False)
            book.uploaded_by = request.user
            book.save() 
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'books/add_book.html', {'form': form})

@login_required
def book_detail(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    return render(request, 'books/book_detail.html', {'book': book})

def edit_book(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    if request.method == 'POST':
        title = request.POST['title']
        author = request.POST['author']
        description = request.POST['description']
        book.title = title
        book.author = author
        book.description = description
        book.save()
        return redirect('book_detail', book_id=book.id)
    return render(request, 'books/edit_book.html', {'book': book})


