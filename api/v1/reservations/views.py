# api/v1/reservation/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from apps.reservation.models import Reservation
from api.v1.reservations.serializers import ReservationSerializer
from rest_framework.permissions import IsAdminUser
from django.shortcuts import get_object_or_404
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

class ReservationListCreateAPIView(APIView):
    permission_classes = [IsAdminUser]
    @swagger_auto_schema(
        tags=["reservation"],
        operation_summary="List all reservations",
        operation_description="Retrieve a list of all book reservations. Admins only.",
        responses={200: ReservationSerializer(many=True)},
    )
    def get(self, request):
        reservations = Reservation.objects.all()
        serializer = ReservationSerializer(reservations, many=True)
        return Response(serializer.data)
    @swagger_auto_schema(
        tags=["reservations"],
        operation_summary="Create a reservation",
        operation_description="Create a new reservation with user, book, date1 and date2 fields. Admins only.",
        request_body=ReservationSerializer,
        responses={201: ReservationSerializer, 400: "Validation errors"},
    )
    def post(self, request):
        serializer = ReservationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ReservationRetrieveUpdateDeleteAPIView(APIView):
    permission_classes = [IsAdminUser]

    def get_object(self, pk):
        return get_object_or_404(Reservation, pk=pk)

    @swagger_auto_schema(
        operation_summary="Retrieve a reservation",
        operation_description="Get a single reservation by its ID. Admins only.",
        responses={200: ReservationSerializer, 404: "Not found"},
    )
    def get(self, request, pk):
        reservation = self.get_object(pk)
        serializer = ReservationSerializer(reservation)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        operation_summary="Update a reservation",
        operation_description="Update all fields of a reservation by its ID. Admins only.",
        request_body=ReservationSerializer,
        responses={200: ReservationSerializer, 400: "Validation errors", 404: "Not found"},
    )
    def put(self, request, pk):
        reservation = self.get_object(pk)
        serializer = ReservationSerializer(reservation, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        operation_summary="Partially update a reservation",
        operation_description="Update some fields of a reservation. Admins only.",
        request_body=ReservationSerializer,
        responses={200: ReservationSerializer, 400: "Validation errors", 404: "Not found"},
    )
    def patch(self, request, pk):
        reservation = self.get_object(pk)
        serializer = ReservationSerializer(reservation, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        operation_summary="Delete a reservation",
        operation_description="Delete a reservation by its ID. Admins only.",
        responses={204: "No content", 404: "Not found"},
    )
    def delete(self, request, pk):
        reservation = self.get_object(pk)
        reservation.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)