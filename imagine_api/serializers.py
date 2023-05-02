from rest_framework import serializers
from .models import ImageModel, UserProfile, Plan, ImageModel

class PlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plan
        fields = '__all__'

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'

class ImageSerializer(serializers.ModelSerializer):

    user_id = serializers.ReadOnlyField(source='user.id')

    class Meta:
        model = ImageModel
        fields =  '__all__'
