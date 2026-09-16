from books.models import Author, Book


# 1. Retrieve all available books
available_books = Book.objects.filter(available=True)


# 2. Retrieve all books by the author with id = 3
books_by_author = Book.objects.filter(author_id=3)


# 3. Retrieve books sorted by publication year (most recent first)
books_by_year = Book.objects.order_by("-publication_year")


# 4. Count the total number of books in the database
total_books = Book.objects.count()


# 5. Create a new book titled 'Les Misérables', available, published in 1862
new_book = Book.objects.create(
    title="Les Misérables",
    publication_year=1862,
    available=True
)