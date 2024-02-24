from django.db import models
from operators.models import Operator
from drivers.models import Driver


class Payment(models.Model):
    driver = models.ForeignKey(Driver, on_delete=models.SET_NULL, null=True)
    operator = models.ForeignKey(Operator, on_delete=models.SET_NULL, null=True)
    date_time = models.DateTimeField(auto_now_add=True)
    amount = models.PositiveIntegerField()
    type = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.driver} --> {self.operator}"
