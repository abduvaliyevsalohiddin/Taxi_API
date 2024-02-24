from django.db import models

from django.contrib.auth.models import AbstractUser


class Customer(AbstractUser):
    role = models.CharField(
        max_length=50,
        choices=(
            ("operator", "operator"),
            ("driver", "driver"),
            ("owner", "owner")
        )
    )
