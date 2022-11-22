from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from vehicles.models import Vehicles
from vehicles.serializers import VehiclesSerializer

from .permissions import isAdmin


# Create your views here.
class VehiclesView(generics.ListCreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [isAdmin]

    queryset = Vehicles.objects.all()
    serializer_class = VehiclesSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
