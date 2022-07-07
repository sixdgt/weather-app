from datetime import datetime
from pyexpat import model
from tkinter import CASCADE
from django.db import models

# Create your models here.
class AppUser(models.Model):
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100, null=True)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    contact = models.CharField(max_length=20)
    dob = models.DateField(default=datetime.now())
    password = models.CharField(max_length=100)
    profile_pic = models.FileField()
    address = models.CharField(max_length=200)
    lat = models.FloatField(null=True, default='0')
    long = models.FloatField(null=True, default='0')
    verification_code = models.CharField(max_length=8)
    is_verified = models.BooleanField(default=False)
    is_removed = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=datetime.now())
    update_at = models.DateTimeField(null=True)
    removed_at = models.DateTimeField(null=True)

    class Meta:
        db_table = "app_user"
    
    def __str__(self):
        return self.first_name

class WeatherType(models.Model):
    weather_type = models.CharField(max_length=100)

    class Meta:
        db_table = "app_weather_type"
    
    def __str__(self):
        return self.weather_type

class Weather(models.Model):
    weather_type = models.ForeignKey(WeatherType, on_delete=models.CASCADE)
    user = models.ForeignKey(AppUser, on_delete=models.CASCADE)
    address = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    updated_at = models.DateTimeField(default=0)

    class Meta:
        db_table = "app_weather"