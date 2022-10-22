from rest_framework import serializers
from . import models

# Model serializer (Allow Django data to be serialized to JSON)

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = '__all__'

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Review
        fields = '__all__'