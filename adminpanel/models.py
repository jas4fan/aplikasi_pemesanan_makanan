from django.db import models

class User(models.Model):
    ROLE_CHOICES = [
        ('customer', 'Customer'),
        ('driver', 'Driver'),
        ('restaurant', 'Restaurant'),
        ('admin', 'Admin'),
    ]
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)

    def __str__(self):
        return self.name

class Driver(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, limit_choices_to={'role': 'driver'})
    phone = models.CharField(max_length=20, blank=True)
    vehicle = models.CharField(max_length=100, blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.user.name} ({'active' if self.is_active else 'inactive'})"

class Rating(models.Model):
    target_user = models.ForeignKey(User, related_name='ratings_received', on_delete=models.CASCADE)
    rater_name = models.CharField(max_length=100, blank=True)
    value = models.IntegerField()  # 1..5
    comment = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.target_user.name} - {self.value}"

