import ipdb
from django.contrib.auth import authenticate
from rest_framework import generics
from rest_framework.authtoken.models import Token

from rest_framework.views import APIView, Request, Response, status
from users.models import User
from users.serializers import UserLoginSerializer, UserSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from .permissions import isAdmin


# Create your views here.
class CreateUserView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [isAdmin]

    queryset = User.objects.all()
    serializer_class = UserSerializer


class LoginView(APIView):
    def post(self, request: Request) -> Response:

        serializer = UserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = authenticate(
            username=serializer.validated_data["username"],
            password=serializer.validated_data["password"],
        )

        if user:
            token, _ = Token.objects.get_or_create(user=user)

            return Response({"token": token.key})

        return Response(
            {"detail": "Invalid username or password"},
            status=status.HTTP_401_UNAUTHORIZED,
        )
