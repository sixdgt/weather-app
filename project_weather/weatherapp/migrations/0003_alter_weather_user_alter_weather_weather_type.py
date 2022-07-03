# Generated by Django 4.0 on 2022-07-03 03:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('weatherapp', '0002_appuser_lat_appuser_long'),
    ]

    operations = [
        migrations.AlterField(
            model_name='weather',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='weatherapp.appuser'),
        ),
        migrations.AlterField(
            model_name='weather',
            name='weather_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='weatherapp.weathertype'),
        ),
    ]
