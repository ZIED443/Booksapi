# api/v1/bookstore/urls.py
from django.urls import path
from .views import (
    BookListCreateAPIView,
    BookRetrieveUpdateDeleteAPIView,
    AuthorListCreateAPIView,
    AuthorRetrieveUpdateDeleteAPIView,
)

urlpatterns = [
    path('books/', BookListCreateAPIView.as_view(), name='book-list-create'),
    path('books/<int:pk>/', BookRetrieveUpdateDeleteAPIView.as_view(), name='book-detail'),
    path('authors/', AuthorListCreateAPIView.as_view(), name='author-list-create'),
    path('authors/<int:pk>/', AuthorRetrieveUpdateDeleteAPIView.as_view(), name='author-detail'),
]
