# Generated by Django 4.2.5 on 2024-03-18 05:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0003_remove_parking_booking_no_slots'),
    ]

    operations = [
        migrations.AddField(
            model_name='parking_booking',
            name='email',
            field=models.CharField(default=1, max_length=40, unique=True),
            preserve_default=False,
        ),
    ]
