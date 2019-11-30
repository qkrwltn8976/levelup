from .models import *
from rest_framework import serializers


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ['name', 'position_x', 'position_y', 'radius']

class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendor
        fields = ['position_x', 'position_y', 'open_time', 'close_time', 'price']

