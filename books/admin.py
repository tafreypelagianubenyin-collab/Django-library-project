from django.contrib import admin

# Register your models here.
from .models import Author, Book


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'name', 'nationality', 'birth_date')
    search_fields = ('name', 'first_name', 'nationality')

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year', 'available')
    list_filter = ('available', 'author', 'publication_year')
    search_fields = ('title', 'author__name', 'author__first_name')