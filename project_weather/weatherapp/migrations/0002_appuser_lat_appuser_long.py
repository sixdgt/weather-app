# Generated by Django 4.0 on 2022-07-03 03:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weatherapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='appuser',
            name='lat',
            field=models.CharField(default='0', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='appuser',
            name='long',
            field=models.CharField(default='0', max_length=100, null=True),
        ),
    ]
