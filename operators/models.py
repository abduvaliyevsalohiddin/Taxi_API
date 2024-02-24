from django.db import models

from drivers.models import Driver
from user.models import Customer


class Operator(Customer):
    email = None
    first_name = None
    last_name = None
    is_staff = None
    is_superuser = None
    ism = models.CharField(max_length=30)
    ish_vaqti = models.CharField(max_length=30)
    tel = models.CharField(max_length=15)

    def __str__(self):
        return self.ism


class Client(models.Model):
    phone = models.CharField(max_length=15)
    total_bonus = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.phone


class Order(models.Model):
    client = models.ForeignKey(Client, on_delete=models.SET_NULL, null=True)
    driver = models.ForeignKey(Driver, on_delete=models.SET_NULL, null=True, blank=True)
    status = models.CharField(
        max_length=20,
        choices=(
            ('active', 'active'),
            ('olindi', 'olindi'),
            ('boshlandi', 'boshlandi'),
            ('yakunlandi', 'yakunlandi'),
            ('bekor qilindi', 'bekor qilindi'),
        )
    )

    total_sum = models.PositiveIntegerField(default=0)
    waiting_seconds = models.PositiveSmallIntegerField(default=0)
    baggage = models.BooleanField(default=False)
    for_women = models.BooleanField(default=False)
    starting_point = models.CharField(max_length=100)
    destination = models.CharField(max_length=100, blank=True, null=True)
    izoh = models.CharField(max_length=100, blank=True, null=True)
    grade = models.PositiveSmallIntegerField(null=True, blank=True)
    date_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.client} --> {self.driver}"

    class Meta:
        ordering = ["-id"]
