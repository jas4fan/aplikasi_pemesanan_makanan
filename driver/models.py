# driver/models.py

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Customer(models.Model):
    name = models.CharField(max_length=100)

class Restaurant(models.Model):
    name = models.CharField(max_length=100)

class DriverProfile(models.Model):
    VEHICLE_CHOICES = [
        ('motorcycle', 'Motor'),
        ('car', 'Mobil'),
        ('bicycle', 'Sepeda'),
    ]
    
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='driver_profile')
    phone = models.CharField(max_length=20)
    vehicle = models.CharField(max_length=50, choices=VEHICLE_CHOICES)
    is_available = models.BooleanField(default=True)
    rating = models.FloatField(default=0.0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.user.get_full_name or self.user.username}"
