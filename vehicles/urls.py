from django import views
from django.urls import path

from .views import VehiclesView

urlpatterns = [
    path("vehicles/", VehiclesView.as_view()),
]
