from rest_framework import serializers
from .models import User


class UserCreateSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=50)
    email = serializers.CharField(max_length=50)
    password = serializers.CharField(min_length=8)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def validate(self, attrs):
        username_exists = User.objects.filter(username=attrs['username']).exists()
        if username_exists:
            raise serializers.ValidationError(detail="Bu User oldin tasdiqlangan ")

        email_exists = User.objects.filter(username=attrs['email']).exists()
        if email_exists:
            raise serializers.ValidationError(detail="User with email exists")

        password_exists = User.objects.filter(username=attrs['password']).exists()
        if password_exists:
            raise serializers.ValidationError(detail="User with password exists")

        return super().validate(attrs)


