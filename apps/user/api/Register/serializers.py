from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=6, max_length=128)  # noqa

    class Meta:
        model = User
        fields = ('username', 'password')

    def create(self, validated_data):
        password = validated_data['password']
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user
