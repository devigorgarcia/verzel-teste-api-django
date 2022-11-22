from django import views
from django.urls import path

from . import views

urlpatterns = [
    path("vehicles/", views.VehiclesView.as_view()),
    path("vehicles/<vehicle_id>/", views.VehicleDetailView.as_view()),
]
