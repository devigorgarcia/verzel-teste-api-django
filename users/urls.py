from django.urls import path
from rest_framework_simplejwt.views import token_obtain_pair

from .views import CreateUserView

urlpatterns = [
    path("users/", CreateUserView.as_view()),
    path("login/", token_obtain_pair),
]
