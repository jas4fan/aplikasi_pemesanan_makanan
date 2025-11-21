from django.db import models

class Order(models.Model):
    customer_name = models.CharField(max_length=100)
    item_name = models.CharField(max_length=100)
    quantity = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.customer_name} - {self.item_name}"

class Rating(models.Model):
    customer_name = models.CharField(max_length=100)
    rating = models.IntegerField()
    comment = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.customer_name} ({self.rating})"

class RestaurantInfo(models.Model):
    restaurant_name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    open_hours = models.CharField(max_length=100)

    def __str__(self):
        return self.restaurant_name

