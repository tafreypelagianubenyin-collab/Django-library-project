from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),                      # Home Page: /
    path('books/', views.book_list, name='book_list'),      # Books List: /books/
    path('books/<int:pk>/', views.book_detail, name='book_detail'),
    path('books/add/', views.add_book, name='add_book'),
]