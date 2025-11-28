from django.contrib import admin
from .models import DriverProfile

@admin.register(DriverProfile)
class DriverProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone', 'vehicle', 'is_available', 'rating')
    list_filter = ('is_available', 'vehicle')
    search_fields = ('user__username', 'phone')
