# api/v1/users/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from apps.users.models import User
from api.v1.users.serializers import UserSerializer
from rest_framework.permissions import IsAdminUser
from django.shortcuts import get_object_or_404
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

class UserListCreateAPIView(APIView):
    permission_classes = [IsAdminUser]
    @swagger_auto_schema(
        tags=["users"],
        operation_summary="List all users",
        operation_description="Retrieve a list of all registered users. Admins only.",
        responses={200: UserSerializer(many=True)},
    )
    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    @swagger_auto_schema(
        tags=["users"],
        operation_summary="Create a new user",
        operation_description="Create a new user with email, password, username, and sex. Admins only.",
        request_body=UserSerializer,
        responses={
            201: UserSerializer,
            400: "Validation errors"
        },
    )
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Retrieve, update, delete a single user
class UserRetrieveUpdateDeleteAPIView(APIView):
    permission_classes = [IsAdminUser]

    def get_object(self, pk):
        return get_object_or_404(User, pk=pk)
    @swagger_auto_schema(
         tags=["users"],
        operation_summary="Retrieve a single user",
        operation_description="Get a single user by their ID. Admins only.",
        responses={200: UserSerializer, 404: "Not found"},
    )
    def get(self, request, pk):
        user = self.get_object(pk)
        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)
    @swagger_auto_schema(
         tags=["users"],
        operation_summary="Update a user",
        operation_description="Update all fields of a user by their ID. Admins only.",
        request_body=UserSerializer,
        responses={200: UserSerializer, 400: "Validation errors", 404: "Not found"},
    )
    def put(self, request, pk):
        user = self.get_object(pk)
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    @swagger_auto_schema(
         tags=["users"],
        operation_summary="Partially update a user",
        operation_description="Update some fields of a user. Admins only.",
        request_body=UserSerializer,
        responses={200: UserSerializer, 400: "Validation errors", 404: "Not found"},
    )
    def patch(self, request, pk):
        user = self.get_object(pk)
        serializer = UserSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    @swagger_auto_schema(
         tags=["users"],
        operation_summary="Delete a user",
        operation_description="Delete a user by their ID. Admins only.",
        responses={204: "No content", 404: "Not found"},
    )
    def delete(self, request, pk):
        user = self.get_object(pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
