from django.contrib import admin
from .models import Order, Rating, RestaurantInfo

admin.site.register(Order)
admin.site.register(Rating)
admin.site.register(RestaurantInfo)


