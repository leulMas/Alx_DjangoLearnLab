from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.authtoken.models import Token   # Token auth

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "email", "bio", "profile_picture", "followers", "following"]
        read_only_fields = ["id", "followers", "following"]


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ["username", "email", "password"]

    def create(self, validated_data):
        user = get_user_model().objects.create_user(
            username=validated_data["username"],
            email=validated_data.get("email", ""),
            password=validated_data["password"],
        )
        # Create auth token automatically
        Token.objects.create(user=user)
        return user
