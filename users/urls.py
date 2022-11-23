from django.urls import path
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView

from .views import CreateUserView, LoginJWTView

urlpatterns = [
    path("users/", CreateUserView.as_view()),
    path("login/", LoginJWTView.as_view()),
    path("schema/", SpectacularAPIView.as_view(), name="schema"),
    path("doc/", SpectacularRedocView.as_view(url_name="schema"), name="redoc"),
]
