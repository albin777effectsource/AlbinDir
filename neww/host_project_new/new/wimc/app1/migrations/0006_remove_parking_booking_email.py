# Generated by Django 4.2.5 on 2024-03-18 05:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0005_alter_parking_booking_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='parking_booking',
            name='email',
        ),
    ]