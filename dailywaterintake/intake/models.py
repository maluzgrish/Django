from django.db import models
from django.contrib.auth.models import User

class Waterintake(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    quantity= models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f'{self.quantity} liters on {self.date}'