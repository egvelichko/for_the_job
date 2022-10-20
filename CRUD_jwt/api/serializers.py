"""System module."""
from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    """create for encode and decode"""
    class Meta:
        """create for api"""
        model = User
        fields = ('id', 'username', 'first_name', 'last_name',
                  'is_active', 'last_login', 'is_superuser')
