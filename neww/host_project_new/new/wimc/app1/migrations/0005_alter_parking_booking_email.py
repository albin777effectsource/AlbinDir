# Generated by Django 4.2.5 on 2024-03-18 05:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0004_parking_booking_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parking_booking',
            name='email',
            field=models.CharField(max_length=40),
        ),
    ]
