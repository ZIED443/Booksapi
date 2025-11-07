# api/v1/bookstore/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from apps.bookstore.models import Book, Author
from api.v1.bookstore.serializers import BookSerializer, AuthorSerializer
from rest_framework.permissions import IsAdminUser
from django.shortcuts import get_object_or_404
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

# -------------------------------
# Author Views
# -------------------------------
class AuthorListCreateAPIView(APIView):
    permission_classes = [IsAdminUser]

    @swagger_auto_schema(
        operation_summary="List all authors",
        operation_description="Retrieve a list of all authors. Admins only.",
        responses={200: AuthorSerializer(many=True)}
    )
    def get(self, request):
        authors = Author.objects.all()
        serializer = AuthorSerializer(authors, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        operation_summary="Create an author",
        operation_description="Create a new author with name and birthday. Admins only.",
        request_body=AuthorSerializer,
        responses={201: AuthorSerializer, 400: "Validation errors"}
    )
    def post(self, request):
        serializer = AuthorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AuthorRetrieveUpdateDeleteAPIView(APIView):
    permission_classes = [IsAdminUser]

    def get_object(self, pk):
        return get_object_or_404(Author, pk=pk)

    @swagger_auto_schema(
        operation_summary="Retrieve an author",
        operation_description="Get a single author by ID. Admins only.",
        responses={200: AuthorSerializer, 404: "Not found"}
    )
    def get(self, request, pk):
        author = self.get_object(pk)
        serializer = AuthorSerializer(author)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        operation_summary="Update an author",
        operation_description="Update all fields of an author. Admins only.",
        request_body=AuthorSerializer,
        responses={200: AuthorSerializer, 400: "Validation errors", 404: "Not found"}
    )
    def put(self, request, pk):
        author = self.get_object(pk)
        serializer = AuthorSerializer(author, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        operation_summary="Partially update an author",
        operation_description="Update some fields of an author. Admins only.",
        request_body=AuthorSerializer,
        responses={200: AuthorSerializer, 400: "Validation errors", 404: "Not found"}
    )
    def patch(self, request, pk):
        author = self.get_object(pk)
        serializer = AuthorSerializer(author, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        operation_summary="Delete an author",
        operation_description="Delete an author by ID. Admins only.",
        responses={204: "No content", 404: "Not found"}
    )
    def delete(self, request, pk):
        author = self.get_object(pk)
        author.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# -------------------------------
# Book Views
# -------------------------------
class BookListCreateAPIView(APIView):
    permission_classes = [IsAdminUser]

    @swagger_auto_schema(
        operation_summary="List all books",
        operation_description="Retrieve a list of all books. Admins only.",
        responses={200: BookSerializer(many=True)}
    )
    def get(self, request):
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        operation_summary="Create a book",
        operation_description="Create a new book with name, author, date_release, total_copies, etc. Admins only.",
        request_body=BookSerializer,
        responses={201: BookSerializer, 400: "Validation errors"}
    )
    def post(self, request):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BookRetrieveUpdateDeleteAPIView(APIView):
    permission_classes = [IsAdminUser]

    def get_object(self, pk):
        return get_object_or_404(Book, pk=pk)

    @swagger_auto_schema(
        tags=["books"],
        operation_summary="Retrieve a book",
        operation_description="Get a single book by ID. Admins only.",
        responses={200: BookSerializer, 404: "Not found"}
    )
    def get(self, request, pk):
        book = self.get_object(pk)
        serializer = BookSerializer(book)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        tags=["books"],
        operation_summary="Update a book",
        operation_description="Update all fields of a book. Admins only.",
        request_body=BookSerializer,
        responses={200: BookSerializer, 400: "Validation errors", 404: "Not found"}
    )
    def put(self, request, pk):
        book = self.get_object(pk)
        serializer = BookSerializer(book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        tags=["books"],
        operation_summary="Partially update a book",
        operation_description="Update some fields of a book. Admins only.",
        request_body=BookSerializer,
        responses={200: BookSerializer, 400: "Validation errors", 404: "Not found"}
    )
    def patch(self, request, pk):
        book = self.get_object(pk)
        serializer = BookSerializer(book, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        tags=["books"],
        operation_summary="Delete a book",
        operation_description="Delete a book by ID. Admins only.",
        responses={204: "No content", 404: "Not found"}
    )
    def delete(self, request, pk):
        book = self.get_object(pk)
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)