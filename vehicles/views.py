from rest_framework import generics
from rest_framework_simplejwt.authentication import JWTAuthentication

from vehicles.models import Vehicles
from vehicles.serializers import VehicleDetailsSerializer, VehiclesSerializer

from .permissions import isAdmin


# Create your views here.
class VehiclesView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [isAdmin]

    queryset = Vehicles.objects.all()
    serializer_class = VehiclesSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class VehicleDetailView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [isAdmin]

    queryset = Vehicles.objects.all()
    serializer_class = VehicleDetailsSerializer

    lookup_url_kwarg = "vehicle_id"
