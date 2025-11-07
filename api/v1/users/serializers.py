from rest_framework import serializers
from apps.users.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "email", "user_name", "role", "is_active", "is_staff"]
        read_only_fields = ["is_staff"]

    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("A user with this email already exists")
        return value

    def validate_role(self, value):
        if value not in dict(User.ROLE_CHOICES):
            raise serializers.ValidationError("Invalid role")
        return value
