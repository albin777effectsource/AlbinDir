from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.parker)
admin.site.register(models.company)
admin.site.register(models.staff)
admin.site.register(models.parkinglot)
admin.site.register(models.parking_booking)
admin.site.register(models.conv_parking)
admin.site.register(models.conv_parking_booking)



