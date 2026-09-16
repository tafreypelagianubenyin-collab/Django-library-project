from django.shortcuts import get_object_or_404, render

from .models import Book

# Create your views here.

def home(request):
    return render(request, "books/home.html")

def book_list(request):
    # Fetch all books so the badges can show available/unavailable status
    books = Book.objects.select_related("author").all()
    return render(request, "books/book_list.html", {"books": books})

def book_detail(request, pk):
    # Safely fetch the book or return a 404 error if not found
    book = get_object_or_404(Book.objects.select_related("author"), pk=pk)
    return render(request, "books/book_detail.html", {"book": book})

def add_book(request):
    return render(request, "books/add_book.html")