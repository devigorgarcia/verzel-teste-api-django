from django.urls import path

from .views import CreateUserView, LoginJWTView

urlpatterns = [
    path("users/", CreateUserView.as_view()),
    path("login/", LoginJWTView.as_view()),
]
