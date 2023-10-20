from django.contrib import admin
from cars.models import Car


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ('model', 'brand', 'factory_year', 'model_year', 'value')
    search_fields = ('model',)
