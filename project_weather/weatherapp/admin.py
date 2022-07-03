from django.contrib import admin
from weatherapp.models import Weather, WeatherType

# Register your models here.
class AdminWeather(admin.ModelAdmin):
    list_display = ('address', 'description')

admin.site.register(Weather, AdminWeather)
admin.site.register(WeatherType)