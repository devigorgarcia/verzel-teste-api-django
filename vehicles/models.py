import uuid

from django.db import models


# Create your models here.
class Vehicles(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    name = models.CharField(max_length=127)
    brand = models.CharField(max_length=127)
    model = models.CharField(max_length=127)
    image = models.CharField(max_length=127)
    price = models.PositiveIntegerField()

    # FK
    user = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="vehicles"
    )
