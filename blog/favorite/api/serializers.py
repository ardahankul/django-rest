from rest_framework.serializers import ModelSerializer
from favorite.models import Favorite
from rest_framework import serializers

class FavoriteCreateSerializer(ModelSerializer):
    class Meta:
        model = Favorite
        fields = '__all__'

    def validate(self, attrs):
        queryset = Favorite.objects.filter(user=attrs["user"],post=attrs["post"])
        if queryset.exists():
            raise serializers.ValidationError("User already liked this post ")
        return attrs        
        