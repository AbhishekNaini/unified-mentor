from django.db import models
from django.contrib.auth.models import User

class Station(models.Model):
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=300)
    latitude = models.FloatField()
    longitude = models.FloatField()
    charger_types = models.CharField(max_length=100)  # Example: "Type1, Type2, DC Fast"
    rate_per_hour = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.name

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    station = models.ForeignKey(Station, on_delete=models.CASCADE)
    date = models.DateField()
    time_slot = models.CharField(max_length=50)  # Example: "10:00 AM - 11:00 AM"
    amount_paid = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Booking {self.id} at {self.station.name}"
