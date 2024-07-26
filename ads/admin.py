from django.contrib import admin
from .models import Location, Ad, Advertisement


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ['name', 'max_visitors', 'latitude', 'longitude', 'address', 'country']


@admin.register(Ad)
class AdAdmin(admin.ModelAdmin):
    list_display = ['name', 'start_date', 'end_date']


@admin.register(Advertisement)
class AdLocationAdmin(admin.ModelAdmin):
    list_display = ['ad', 'location', 'daily_visitors', 'blocked']
