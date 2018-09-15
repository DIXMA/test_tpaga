from django.contrib.auth.models import User
from rest_framework import serializers
from app.models import Account


class UserSerializer(serializers.ModelSerializer):
    """
    Serializer for User Model
    @author: Diego Cortés <ingdiego.corts65@gmial.com>
    """
    class Meta:
        model = User
        fields = ('username', 'email')


class AccountSerializer(serializers.ModelSerializer):
    """
    Serializer for Account Model
    @author: Diego Cortés <ingdiego.corts65@gmial.com>
    """
    class Meta:
        model = Account
        fields = '__all__'
