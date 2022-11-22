from django import views
from django.urls import path


from .views import CreateUserView,LoginView

urlpatterns = [
    path("users/", CreateUserView.as_view()),
     path("login/", LoginView.as_view()),
]
