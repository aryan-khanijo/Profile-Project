from rest_framework import serializers
from . import models

class HelloSerializer(serializers.Serializer):
    """Serializes a name field for testing our APIView"""
    name = serializers.CharField(max_length = 10)


class UserProfileSerializer(serializers.ModelSerializer):
    """Serializes a user profile"""

    class Meta:
        model = models.UserProfile
        exclude = ('last_login','is_active','is_admin')
        extra_kwargs = {
            'password': {
                'write_only' : True,
                'style': {'input_type': 'password'}
            }
        }

    def create(self, validated_data):
        """Create a new User"""
        user = models.UserProfile.objects.create_user(
            name = validated_data['name'],
            email = validated_data['email'],
            password = validated_data['password']
        )

        return user


class ProfileFeedItemSerializer(serializers.ModelSerializer):
    """Serializes profile feed items"""
    class Meta:
        model = models.ProfileFeedItem
        fields = '__all__'
        extra_kwargs = {'user_profile': {'read_only': True}}
