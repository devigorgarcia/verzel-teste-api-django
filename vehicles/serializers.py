from rest_framework import serializers

from users.serializers import UserSerializer

from .models import Vehicles


class VehiclesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicles
        fields = "__all__"
        read_only_fields = ["user"]


class VehicleDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicles
        fields = "__all__"

    user = UserSerializer(read_only=True)
