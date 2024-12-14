from rest_framework import serializers
from .models import CustomUser
from rest_framework.authtoken.models import Token
from django.contrib.auth import get_user_model

# Get the user model 
User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'bio', 'profile_picture', 'followers')


class UserRegisterSerializer(serializers.ModelSerializer):
    username = serializers.CharField()  # Explicitly declared
    email = serializers.EmailField()    # Explicitly declared
    password = serializers.CharField()


    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'password', 'email', 'bio', 'profile_picture']

    def create(self, validated_data):
        user = get_user_model().objects.create_user(**validated_data)
        Token.objects.create(user=user)
        return user