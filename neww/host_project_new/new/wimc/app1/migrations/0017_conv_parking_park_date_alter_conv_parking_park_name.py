# Generated by Django 4.2.5 on 2024-04-03 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0016_conv_parking'),
    ]

    operations = [
        migrations.AddField(
            model_name='conv_parking',
            name='park_date',
            field=models.CharField(default=1, max_length=16),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='conv_parking',
            name='park_name',
            field=models.TextField(max_length=40),
        ),
    ]
