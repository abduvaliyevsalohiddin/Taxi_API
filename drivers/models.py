from django.db import models


class CarCategory(models.Model):
    type = models.CharField(max_length=30)
    minium = models.PositiveIntegerField()
    sum_per_km = models.PositiveIntegerField()
    waiting_cost = models.PositiveIntegerField()
    baggage_cost = models.PositiveIntegerField()
    bonus_percent = models.PositiveSmallIntegerField()
    firm_percent = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.type


class Driver(models.Model):
    last_name = None
    email = None
    first_name = None
    is_staff = None
    is_superuser = None
    fullname = models.CharField(max_length=30)
    phone = models.CharField(max_length=30)
    photo = models.FileField(upload_to='drivers', blank=True, null=True)
    car_type = models.CharField(max_length=30)
    car_number = models.CharField(max_length=10)
    birth_date = models.DateField()
    sms_code = models.CharField(max_length=7)
    balance = models.PositiveIntegerField(default=0)
    confirmed = models.BooleanField(default=False)
    gender = models.CharField(max_length=10, default="Erkak")
    has_baggage = models.BooleanField(default=True)
    category = models.ForeignKey(CarCategory, on_delete=models.SET_NULL, null=True)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.fullname

    class Meta:
        ordering = ["-id"]
