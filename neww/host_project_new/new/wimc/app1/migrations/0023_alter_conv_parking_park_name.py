# Generated by Django 4.2.5 on 2024-04-13 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0022_company_park_price_company_park_slots'),
    ]

    operations = [
        migrations.AlterField(
            model_name='conv_parking',
            name='park_name',
            field=models.CharField(max_length=100),
        ),
    ]
