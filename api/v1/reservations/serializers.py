from rest_framework import serializers
from apps.reservation.models import Reservation

class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = ["id", "user", "book", "start_date", "end_date" ]

    def validate(self, attrs):
        if attrs["end_date"] <= attrs["start_date"]:
            raise serializers.ValidationError({"end_date": "End date must be after start date"})
        return attrs
