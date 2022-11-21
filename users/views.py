from rest_framework import generics

from users.models import User
from users.serializers import UserSerializer


# Create your views here.
class CreateUserView(generics.ListCreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
