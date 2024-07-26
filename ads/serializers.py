from rest_framework import serializers
from .models import Ad, Location, Advertisement


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'


class AdSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ad
        fields = '__all__'


class AdvertisementSerializer(serializers.ModelSerializer):
    ad = AdSerializer(read_only=True)
    location = LocationSerializer(read_only=True)

    class Meta:
        model = Advertisement
        fields = '__all__'
