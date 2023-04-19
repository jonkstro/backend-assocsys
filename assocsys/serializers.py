from django.contrib.auth.models import User
from rest_framework import serializers
from django.contrib.auth.hashers import make_password

# Serializer que realizará as autenticações dos Users


class UserCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)
    username = serializers.CharField(write_only=True, required=False)

    class Meta:
        model = User
        fields = ['id',
                  'username',
                  'email',
                  'password',
                  'first_name',
                  'is_active'
                  ]

    def create(self, validated_data):
        validated_data['password'] = make_password(
            validated_data.get('password')
        )
        validated_data['is_active'] = False
        # estamos definindo abaixo que o campo USERNAME será igual ao campo EMAIL, 
        # para realizar a validação por EMAIL ao invés de Username
        validated_data['username'] = validated_data['email']

        return super(UserCreateSerializer, self).create(validated_data)
