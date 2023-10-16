from django.contrib import admin
from .models import Car  # Import the Car model from your models.py

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ('make', 'model', 'year', 'price')
    list_filter = ('make', 'year')
    search_fields = ('make', 'model', 'year')
    prepopulated_fields = {'slug': ('make', 'model')}
