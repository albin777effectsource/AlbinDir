import datetime

from django.db import models
from django.core.validators import validate_image_file_extension
from django.utils import timezone
# Create your models here.
class parker(models.Model):
    name = models.CharField(max_length=30)
    ph_no = models.IntegerField()
    email = models.CharField(max_length=40,unique=True)
    password = models.CharField(max_length=40)
    def __str__(self):
        return self.name

class company(models.Model):
    cname = models.CharField(max_length=50)
    c_logo= models.ImageField(upload_to='static/img/company_profile_pics', validators=[validate_image_file_extension])
    c_ph_no = models.IntegerField()
    park_option = models.TextField(max_length=25)
    timeA = models.TimeField()
    timeZ = models.TimeField()
    c_location = models.CharField(max_length=40)
    c_desc = models.TextField(max_length=500)
    park_slots = models.IntegerField()
    park_price = models.IntegerField()
    c_email = models.CharField(max_length=40,unique=True)
    c_pswd = models.CharField(max_length=40)
    def __str__(self):
        return self.cname

class staff(models.Model):
    s_name = models.CharField(max_length=20)
    cname = models.CharField(max_length=20)
    prof_pic = models.ImageField(upload_to='static/img/staff_profile_pics', validators=[validate_image_file_extension])
    job_desc = models.CharField(max_length=40)
    s_ph_no = models.IntegerField()
    c_email = models.CharField(max_length=40)
    c_location = models.CharField(max_length=40)
    s_email = models.CharField(max_length=40)
    s_password = models.CharField(max_length=40)
    def __str__(self):
        return self.s_name

class parkinglot(models.Model):
    park_type = models.CharField(max_length=20)
    park_id = models.IntegerField()
    park_cname = models.CharField(max_length=20)
    park_c_location = models.CharField(max_length=40)
    park_c_email = models.CharField(max_length=40)
    park_c_ph_no = models.IntegerField()
    start_time = models.IntegerField()
    end_time = models.IntegerField()
    no_slots = models.IntegerField()
    park_price = models.FloatField()
    extra_price = models.FloatField()
    def __str__(self):
        return self.park_c_email


class parking_booking(models.Model):
    user_details=models.ForeignKey(parker,on_delete=models.CASCADE)
    park_details=models.ForeignKey(parkinglot, on_delete=models.CASCADE)
    park_price =models.FloatField()
    no_hrs = models.IntegerField()
    start_time = models.CharField(max_length=10)
    end_time = models.CharField(max_length=10)
    Email = models.CharField(max_length=40)
    booked_date = models.CharField(max_length=10)

class conv_parking(models.Model):
    company_details=models.ForeignKey(company, on_delete=models.CASCADE)
    park_name = models.CharField(max_length=100)
    park_date = models.CharField(max_length=16)
    park_email = models.CharField(max_length=50)
    stock_item = models.IntegerField()
    park_price = models.FloatField()
    def __str__(self):
        return self.park_email

class conv_parking_booking(models.Model):
    user_details=models.ForeignKey(parker,on_delete=models.CASCADE)
    park_details=models.ForeignKey(conv_parking, on_delete=models.CASCADE)
    Email = models.CharField(max_length=40)
    phone_no = models.IntegerField()
    park_date = models.CharField(max_length=10)
    no_slots = models.IntegerField()
    park_price =models.FloatField()
