# api/v1/reservation/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from apps.reservation.models import Reservation
from api.v1.reservations.serializers import ReservationSerializer
from rest_framework.permissions import IsAdminUser
from django.shortcuts import get_object_or_404

class ReservationListCreateAPIView(APIView):
    permission_classes = [IsAdminUser]

    def get(self, request):
        reservations = Reservation.objects.all()
        serializer = ReservationSerializer(reservations, many=True)
        return Response(serializer.data)

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

    def get(self, request, pk):
        reservation = self.get_object(pk)
        serializer = ReservationSerializer(reservation)
        return Response(serializer.data)

    def put(self, request, pk):
        reservation = self.get_object(pk)
        serializer = ReservationSerializer(reservation, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        reservation = self.get_object(pk)
        serializer = ReservationSerializer(reservation, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        reservation = self.get_object(pk)
        reservation.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
