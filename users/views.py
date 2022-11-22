from rest_framework import generics
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.views import TokenObtainPairView

from users.models import User
from users.serializers import MyCustomTokenSerializer, UserSerializer

from .permissions import isAdmin


# Create your views here.
class CreateUserView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [isAdmin]

    queryset = User.objects.all()
    serializer_class = UserSerializer


class LoginJWTView(TokenObtainPairView):
    serializer_class = MyCustomTokenSerializer  # vindo do serializer criado antes
