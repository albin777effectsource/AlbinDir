import datetime
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from django.contrib import messages
from .models import parkinglot
import razorpay
import datetime
from .models import parking_booking
from django.core.exceptions import ValidationError
from django.core.validators import validate_email, RegexValidator
from django.core.validators import validate_image_file_extension
from django.contrib.auth.password_validation import validate_password
from django.utils import timezone
from django.core.mail import send_mail


# Create your views here.
def index(re):
    data1 = company.objects.all()
    data2 = parkinglot.objects.all()

    return render(re, 'index.html',{'data1':data1,'data2':data2})

def dark_index(re):
    data1 = company.objects.all()
    data2 = parkinglot.objects.all()

    return render(re, 'dark_index.html',{'data1':data1,'data2':data2})

def about(re):
    return render(re, 'about.html')


def contact(re):
    return render(re, 'contact.html')


def feature(re):
    return render(re, 'feature.html')

def service(re):
    return render(re, 'service.html')


def quote(re):
    return render(re, 'quote.html')


def team(re):
    data1 = company.objects.all()
    return render(re, 'team.html',{'data1':data1})


def testimonial(re):
    return render(re, 'testimonial.html')




def register(re):
    if re.method == 'POST':
        name = re.POST['name']
        phone_number = re.POST['ph_no']
        email = re.POST['email']
        password = re.POST['password']
        if not name:
            messages.error(re, 'Name cannot be blank')
            return redirect(register)
        # Validate phone number (Indian format)
        phone_validator = RegexValidator(regex=r'^\d{10}$', message="Phone number must be entered in the format: '9896888739'. Up to 10 digits allowed.")
        try:
            phone_validator(phone_number)
        except ValidationError as e:
            messages.error(re, str(e))
            return redirect(register)
        try:
            validate_email(email)
        except ValidationError as e:
            messages.error(re, str(e))
            return redirect(register)
        try:
            validate_password(password)
        except ValidationError as e:
            messages.error(re, str(e))
            return redirect(register)
        try:
            data = parker.objects.create(name=name, ph_no=phone_number, email=email, password=password)
            data.save()
            messages.success(re, 'Registered successfully')
            return redirect(register)
        except Exception as e:
            messages.error(re, 'Email already exists. error:' + str(e))
            return redirect(register)
    else:
        # re.session['email'] = send_mail
        return render(re, 'register.html')


def login(re):
    if re.method == 'POST':
        email = re.POST['email']
        password = re.POST['password']
        try:
            data = parker.objects.get(email=email)
            if data.password == password:
                re.session['user'] = email
                return redirect(user_index)
            else:
                messages.error(re, 'password incorrect')
                return render('login.html')
        except Exception:
            try:
                data = company.objects.get(c_email=email)
                if data.c_pswd == password:
                    re.session['c_id'] = email
                    return redirect(company_index)
                else:
                    messages.error(re, 'password incorrect')
                    return render(re, "login.html")
            except Exception:
                try:
                    data = staff.objects.get(s_email=email)
                    if data.s_password == password:
                        re.session['s_id'] = email
                        return redirect(staff_index)
                    else:
                        messages.error(re, 'password incorrect')
                        return render(re, "login.html")
                except Exception:
                    if email == 'admin@123' and password == 'admin$123':
                        re.session['id1'] = email
                        return redirect(admin_index)
                    else:
                        messages.error(re, 'email incorrect')
                        return redirect(login)
    else:
        return render(re, 'login.html')

def e404(re):
    return render(re, 'e404.html')

def user_index(re):
    data=parker.objects.get(email=re.session['user'])
    data1 = company.objects.all()
    return render(re, 'user_dir/user_index.html',{'data':data,'data1':data1})


def admin_index(re):
    data = company.objects.all()
    return render(re,'project_admin/admin_index.html',{'data':data})


def company_register(re):
    if re.method == 'POST':
        a = re.POST['cname']
        b = re.FILES.get('c_logo')
        c = re.POST['c_ph_no']
        d = re.POST.get('park_option')
        g = re.POST['timeA']
        h = re.POST['timeZ']
        i = re.POST['c_location']
        j = re.POST['c_desc']
        k = re.POST['park_slots']
        l = re.POST['park_price']
        m = re.POST['c_email']
        n = re.POST['c_pswd']
        if not a:
            messages.error(re, 'Name cannot be blank')
            return redirect(company_register)
        if not b:
            messages.error(re, 'Logo cannot be blank')
            return redirect(company_register)
        else:
            phone_validator = RegexValidator(regex=r'^\d{10}$',message="Phone number must be entered in the format: '9896888739'. Up to 10 digits allowed.")
        try:
            phone_validator(c)
        except ValidationError as e:
            messages.error(re, str(e))
            return redirect(company_register)
        if not d:
            messages.error(re, 'Park option must be selected')
            return redirect(company_register)
        if not g:
            messages.error(re, 'Park place opening Time must be selected')
            return redirect(company_register)
        if not h:
            messages.error(re, 'Park place closing Time must be selected')
            return redirect(company_register)
        if not i:
            messages.error(re, 'Location cannot be blank')
            return redirect(company_register)
        if not j:
            messages.error(re, 'Company description is required')
            return redirect(company_register)
        if not k:
            messages.error(re, 'Company parking slots is required')
            return redirect(company_register)
        if not l:
            messages.error(re, 'Company parking price is required')
            return redirect(company_register)
        try:
            validate_email(m)
        except ValidationError as e:
            messages.error(re, str(e))
            return redirect(company_register)
        try:
            validate_password(n)
        except ValidationError as e:
            messages.error(re, str(e))
            return redirect(company_register)
        try:
            data = company.objects.create(cname=a, c_logo=b, c_ph_no=c, park_option=d, timeA=g, timeZ=h, c_location=i, c_desc=j, park_slots=k, park_price=l, c_email=m, c_pswd=n)
            data.save()
            messages.success(re, 'company_registered successfully')
            return redirect(company_register)
        except Exception:
            messages.error(re, 'email already used')
            return redirect(company_register)
    else:
        return render(re, 'company_register.html')



def disp_user(re):
    data = parker.objects.all()
    return render(re,'project_admin/disp_user.html',{'data':data})

def company_index(re):
    data = company.objects.get(c_email=re.session['c_id'])
    our_staff_data = staff.objects.filter(c_email=re.session['c_id'])
    data4 = parkinglot.objects.filter(park_c_email=re.session['c_id'])
    return render(re,'company/company_index.html',{'data':data,'our_staff_data':our_staff_data,'data4':data4})

def staff_register(re):
    if re.method == 'POST':
        a = re.POST['s_name']
        b = re.POST['cname']
        c = re.FILES.get('prof_pic')
        d = re.POST['job_desc']
        e = re.POST['s_ph_no']
        f = re.POST['c_email']
        g = re.POST['c_location']
        h = re.POST['s_email']
        i = re.POST['s_password']
        if not a:
            messages.error(re, 'Staff name cannot be blank')
            return redirect(staff_register)
        if not c:
            messages.error(re, 'Logo cannot be blank')
            return redirect(staff_register)
        if not d:
            messages.error(re, 'Job Description must be selected')
            return redirect(staff_register)
        else:
            phone_validator = RegexValidator(regex=r'^\d{10}$',message="Phone number must be entered in the format: '9896888739'. Up to 10 digits allowed.")
        try:
            phone_validator(e)
        except ValidationError as e:
            messages.error(re, str(e))
            return redirect(staff_register)
        try:
            validate_email(h)
        except ValidationError as e:
            messages.error(re, str(e))
            return redirect(staff_register)
        try:
            validate_password(i)
        except ValidationError as e:
            messages.error(re, str(e))
            return redirect(staff_register)
        try:
            data = staff.objects.create(s_name=a, cname=b, prof_pic=c, job_desc=d, s_ph_no=e, c_email=f, c_location=g, s_email=h, s_password=i)
            data.save()
            messages.success(re, 'Registered successfully')
            return redirect(staff_register)
        except Exception:
            messages.error(re, 'email already used')
            return redirect(staff_register)
    else:
        data=company.objects.get(c_email=re.session['c_id'])
        print(data)
        return render(re,'staff/Staff_register.html',{'data':data})

# def disp_park_logo(re):
#     data1 = company.objects.all()
#     return render(re,'user_dir/user_index.html',{'data1':data1})
def disp_staff_details(re):
    s_details = staff.objects.all()
    return render(re,'project_admin/disp_staff_details.html',{'s_details':s_details})
def disp_park2(re):
    data = company.objects.all()
    return render(re,'project_admin/admin_index.html',{'data':data})

def staff_index(re):
    data = staff.objects.get(s_email=re.session['s_id'])
    return render(re,'staff/Staff_index.html',{'data':data})

def staff_view_company_details(re):
    data = company.objects.all()
    return render(re,'staff/Staff_index.html',{'data':data})

def park_book(re,id):
    data1 =company.objects.get(pk=id)
    return render(re,'user_dir/park_bookv2.html',{'data1':data1})


def our_staff(re):
    data = company.objects.get(c_email=re.session['c_id'])
    our_staff_data = staff.objects.filter(c_email=re.session['c_id'])
    return render(re,'company/our_staff.html',{'data':data,'our_staff_data':our_staff_data})

def company_admin_edit(re,id):
    if re.method == 'POST':

        a = re.POST['cname']
        b = re.POST.get('c_logo', None)
        c = re.POST['c_ph_no']
        d = re.POST['park_option']
        g = re.POST['timeA']
        h = re.POST['timeZ']
        j = re.POST['c_location']
        k = re.POST['c_email']
        l = re.POST['c_pswd']
        company.objects.filter(pk=id).update(cname=a,c_logo=b,c_ph_no=c,park_option=d,timeA=g,timeZ=h,c_location=j,c_email=k,c_pswd=l)
        messages.success(re, 'Updated successfully')
        return redirect(disp_park2)
    else:
        data=company.objects.get(pk=id)
        return render(re, 'project_admin/company_admin_edit.html', {'data': data})

def company_edit(re,id):
    if re.method == 'POST':
        a = re.POST['cname']
        b = re.FILES.get('c_logo')
        c = re.POST['c_ph_no']
        d = re.POST.get('park_option')
        g = re.POST['timeA']
        h = re.POST['timeZ']
        i = re.POST['c_location']
        j = re.POST['c_desc']
        k = re.POST['park_slots']
        l = re.POST['park_price']
        m = re.POST['c_email']
        n = re.POST['c_pswd']
        if not a:
            messages.error(re, 'Name cannot be blank')
            return redirect(company_edit)
        if not b:
            messages.error(re, 'Logo cannot be blank')
            return redirect(company_edit)
        else:
            phone_validator = RegexValidator(regex=r'^\d{10}$',message="Phone number must be entered in the format: '9896888739'. Up to 10 digits allowed.")
        try:
            phone_validator(c)
        except ValidationError as e:
            messages.error(re, str(e))
            return redirect(company_edit)
        if not d:
            messages.error(re, 'Park option must be selected')
            return redirect(company_edit)
        if not g:
            messages.error(re, 'Park place opening Time must be selected')
            return redirect(company_edit)
        if not h:
            messages.error(re, 'Park place closing Time must be selected')
            return redirect(company_edit)
        if not i:
            messages.error(re, 'Location cannot be blank')
            return redirect(company_edit)
        if not j:
            messages.error(re, 'Company description is required')
            return redirect(company_edit)
        if not k:
            messages.error(re, 'Company parking slots is required')
            return redirect(company_edit)
        if not l:
            messages.error(re, 'Company parking price is required')
            return redirect(company_edit)
        try:
            validate_email(m)
        except ValidationError as e:
            messages.error(re, str(e))
            return redirect(company_edit)
        try:
            validate_password(n)
        except ValidationError as e:
            messages.error(re, str(e))
            return redirect(company_edit)
        company.objects.filter(pk=id).update(cname=a, c_logo=b, c_ph_no=c, park_option=d, timeA=g, timeZ=h, c_location=i, c_desc=j, park_slots=k, park_price=l, c_email=m, c_pswd=n)
        messages.success(re, 'Updated successfully')
        return redirect(company_index)
    else:
        data=company.objects.get(pk=id)
        return render(re, 'company/company_edit.html', {'data': data})



def add_parking_lot(re):
    if re.method == 'POST':
        park_type = re.POST['pname']
        park_id = re.POST['id']
        park_cname = re.POST['cname']
        park_c_location = re.POST['c_location']
        park_c_email = re.POST['c_email']
        park_c_ph_no = re.POST['c_ph_no']
        start_time = re.POST['timeA']
        end_time = re.POST['timeZ']
        no_slots = re.POST['stock']
        park_price = re.POST['price']
        extra_price = re.POST['xtr_price']
        data = parkinglot.objects.create(park_type=park_type,park_id=park_id, park_cname=park_cname, park_c_location=park_c_location, park_c_email=park_c_email, park_c_ph_no=park_c_ph_no, start_time=start_time, end_time=end_time, no_slots=no_slots, park_price=park_price ,extra_price=extra_price)
        data.save()
        messages.success(re, 'Registered successfully')
        return redirect(add_parking_lot)
    else:
        data=company.objects.get(c_email=re.session['c_id'])
        return render(re,'company/add_parking_lot.html',{'data':data})





def parking_booking_user_view(re,id):
    data=parker.objects.get(email=re.session['user'])
    data1 = parking_booking.objects.filter(park_details=id)
    return render(re,'user_dir/parking_booking_user_view.html',{'data':data,'data1':data1})


def parking_lot_company_view(re):
    data = company.objects.get(c_email=re.session['c_id'])
    data4 = parkinglot.objects.filter(park_c_email=re.session['c_id'])
    return render(re, 'company/parking_lot_company_view.html',{'data':data,'data4':data4})


###############################<<<  Payment Section Start >>>>#########################################################



def success(re):
    messages.success(re, 'Payment success')
    return redirect(user_index)

###############################<<<  Payment Section End >>>>#########################################################


def user_booked_details(re):
    data = parker.objects.get(email=re.session['user'])
    data1=parking_booking.objects.filter(user_details=data)
    return render(re,'user_dir/user_booked_details.html',{'data':data,'data1':data1})

def user_admin_edit(re,id):
    if re.method == 'POST':
        a = re.POST['name']
        b = re.POST['ph_no']
        c = re.POST['email']
        d = re.POST['password']
        parker.objects.filter(pk=id).update(name=a,ph_no=b,email=c,password=d)
        messages.success(re, 'Updated successfully')
        return redirect(disp_staff_details)
    else:
        data=parker.objects.get(pk=id)
        return render(re, 'project_admin/user_admin_edit.html', {'data': data})


# user_profile_edit
def user_profile_edit(re,id):
    if re.method == 'POST':
        a = re.POST['name']
        b = re.POST['ph_no']
        c = re.POST['email']
        d = re.POST['password']
        if not a:
            messages.error(re, 'Name cannot be blank')
            return redirect(user_profile_edit)
        phone_validator = RegexValidator(regex=r'^\d{10}$', message="Phone number must be entered in the format: '98968XXXX9'. Up to 10 digits allowed.")
        try:
            phone_validator(b)
        except ValidationError as e:
            messages.error(re, str(e))
            return redirect(user_profile_edit)
        try:
            validate_email(c)
        except ValidationError as e:
            messages.error(re, str(e))
            return redirect(user_profile_edit)
        try:
            validate_password(d)
        except ValidationError as e:
            messages.error(re, str(e))
            return redirect(user_profile_edit)
        parker.objects.filter(pk=id).update(name=a,ph_no=b,email=c,password=d)
        messages.success(re, 'Updated successfully')
        return redirect(user_index)
    else:
        data=parker.objects.get(pk=id)
        return render(re, 'user_dir/user_profile_edit.html', {'data': data})

def staff_company_edit(re,id):
    if re.method == 'POST':
        a = re.POST['s_name']
        b = re.POST['cname']
        j = re.POST['prof_pic']
        i = re.POST['job_desc']
        c = re.POST['s_ph_no']
        d = re.POST['c_email']
        f = re.POST['c_location']
        g = re.POST['s_email']
        h = re.POST['s_password']
        staff.objects.filter(pk=id).update(s_name=a, cname=b, prof_pic=j, job_desc=i, s_ph_no=c, c_email=d, c_location=f, s_email=g, s_password=h)
        messages.success(re, 'Updated successfully')
        return redirect(company_index)
    else:
        data = staff.objects.get(pk=id)
        return render(re, 'company/staff_company_edit.html', {'data': data})


def staff_admin_edit(re,id):
    if re.method == 'POST':
        a = re.POST['s_name']
        b = re.POST['cname']
        j = re.POST['prof_pic']
        i = re.POST['job_desc']
        c = re.POST['s_ph_no']
        d = re.POST['c_email']
        f = re.POST['c_location']
        g = re.POST['s_email']
        h = re.POST['s_password']
        staff.objects.filter(pk=id).update(s_name=a, cname=b, prof_pic=j, job_desc=i, s_ph_no=c, c_email=d, c_location=f, s_email=g, s_password=h)
        messages.success(re, 'Updated successfully')
        return redirect(admin_index)
    else:
        data = staff.objects.get(pk=id)
        return render(re, 'project_admin/staff_admin_edit.html', {'data': data})

def parking_lot_company_edit(re,id):
    if re.method == 'POST':
        park_type = re.POST['pname']
        park_id = re.POST['id']
        park_cname = re.POST['cname']
        park_c_location = re.POST['c_location']
        park_c_email = re.POST['c_email']
        park_c_ph_no = re.POST['c_ph_no']
        start_time = re.POST['timeA']
        end_time = re.POST['timeZ']
        no_slots = re.POST['stock']
        park_price = re.POST['price']
        extra_price = re.POST['xtr_price']
        parkinglot.objects.filter(pk=id).update(park_type=park_type,park_id=park_id,park_cname=park_cname,park_c_location=park_c_location,park_c_email=park_c_email,park_c_ph_no=park_c_ph_no,start_time=start_time,end_time=end_time,no_slots=no_slots,park_price=park_price,extra_price=extra_price)
        messages.success(re, 'Updated successfully')
        return redirect(parking_lot_company_view)
    else:
        data4=parkinglot.objects.get(pk=id)
        return render(re, 'company/parking_lot_company_edit.html', {'data4': data4})

def staff_edit(re,id):
    if re.method == 'POST':
        a = re.POST['s_name']
        b = re.POST['cname']
        j = re.POST['prof_pic']
        i = re.POST['job_desc']
        c = re.POST['s_ph_no']
        d = re.POST['c_email']
        f = re.POST['c_location']
        g = re.POST['s_email']
        h = re.POST['s_password']
        staff.objects.filter(pk=id).update(s_name=a,cname=b,prof_pic=j,job_desc=i,s_ph_no=c,c_email=d,c_location=f,s_email=g,s_password=h)
        messages.success(re, 'Updated successfully')
        return redirect(staff_index)
    else:
        data=staff.objects.get(pk=id)
        return render(re, 'staff/Staff_edit.html', {'data': data})


# def park_book_staff_view(re,id):
#     data =company.objects.get(pk=id)
#     data1 = parker.objects.filter(email=re.session['user'])
#     data2=parking_booking.objects.filter(user_details=data)
#     return render(re,'company/park_book_staff_view.html',{'data':data,'data1':data1,'data2':data2})
#

def company_outsider_view(re,id):
    data1 =company.objects.get(pk=id)
    return render(re,'company_outsider_view.html',{'data1':data1})

def delete_staff_by_company(re,id):
    data=staff.objects.filter(pk=id)
    data.delete()
    messages.success(re,"successfully deleted staff")
    return redirect(company_index)

def delete_company_by_admin(re,id):
    data=company.objects.filter(pk=id)
    data.delete()
    messages.success(re,"successfully deleted company")
    return redirect(admin_index)

def delete_staff_by_admin(re,id):
    data=staff.objects.filter(pk=id)
    data.delete()
    messages.success(re,"successfully deleted staff")
    return redirect(admin_index)

def delete_user_by_admin(re,id):
    data=parker.objects.filter(pk=id)
    data.delete()
    messages.success(re,"successfully deleted user")
    return redirect(admin_index)

def delete_parking_lot_by_company(re,id):
    data=parkinglot.objects.filter(pk=id)
    data.delete()
    messages.success(re,"successfully deleted parking_lot")
    return redirect(company_index)

def company_user_view(re,id):
    data = parker.objects.get(email=re.session['user'])
    data1 =company.objects.get(pk=id)
    return render(re,'user_dir/company_user_view.html',{'data':data,'data1':data1})

def cancel_booking_by_user(re,id):
    data=parking_booking.objects.filter(pk=id)
    data.delete()
    messages.success(re,"successfully canceled booking")
    return redirect(user_index)

def parkinglot_admin_view(re):
    data = parkinglot.objects.all()
    return render(re,'project_admin/parkinglot_admin_view.html',{'data':data})



# parking_booking_admin_view
def parking_booking_admin_view(re,id):
    data1 = parking_booking.objects.filter(park_details=id)
    return render(re,'project_admin/parking_booking_admin_view.html',{'data1':data1})




def all_parking_booking_admin_view(re):
    data2 = parking_booking.objects.all()
    return render(re,'project_admin/all_parking_booking_admin_view.html',{'data2':data2})

def booking_company_view(re, id):
    data = company.objects.get(c_email=re.session['c_id'])
    data1 = parking_booking.objects.filter(park_details=id)
    return render(re, 'company/booking_company_view.html', {'data': data,'data1': data1})

def parking_lot_staff_view(re):
    data4 = conv_parking.objects.all()
    data = staff.objects.get(s_email=re.session['s_id'])
    return render(re, 'staff/parking_lot_staff_view.html', {'data4': data4,'data': data})

def parking_booking_staff_view(re, id):
    data = staff.objects.get(s_email=re.session['s_id'])
    data1 = parking_booking.objects.filter(park_details=id)
    return render(re,'staff/parking_booking_staff_view.html',{'data': data,'data1':data1})


def company_settings(re):
    data = company.objects.get(c_email=re.session['c_id'])
    our_staff_data = staff.objects.filter(c_email=re.session['c_id'])
    data4 = parkinglot.objects.filter(park_c_email=re.session['c_id'])
    return render(re,'company/company_settings.html',{'data':data,'our_staff_data':our_staff_data,'data4':data4})


def delete_conv_parking_by_company(re,id):
    data=conv_parking.objects.filter(pk=id)
    data.delete()
    messages.success(re,"successfully deleted parking_lot")
    return redirect(conv_parking_company_view)

def add_conv_parking(re):
    if re.method == 'POST':
        company_details = company.objects.get(c_email=re.session['c_id'])
        park_name = re.POST['park_name']
        park_date = re.POST['park_date']
        park_email = re.POST['park_email']
        stock_item = re.POST['stock']
        park_price = re.POST['price']
        data = conv_parking.objects.create(company_details=company_details,park_name=park_name,park_date=park_date,park_email=park_email, stock_item=stock_item , park_price=park_price)
        data.save()
        messages.success(re, 'Registered successfully')
        return redirect(add_conv_parking)
    else:
        data=company.objects.get(c_email=re.session['c_id'])
        return render(re,'company/add_conv_parking.html',{'data':data})


def conv_parking_company_view(re):
    data = company.objects.get(c_email=re.session['c_id'])
    data2 = conv_parking.objects.filter(park_email=re.session['c_id'])
    return render(re, 'company/conv_parking_company_view.html',{'data':data,'data2':data2})

def user_conv_parking_view(re):
    data=parker.objects.get(email=re.session['user'])
    data1 = company.objects.all()
    return render(re, 'user_dir/user_conv_parking_view.html',{'data':data,'data1':data1})

def parking_lot_user_view(re):
    data=parker.objects.get(email=re.session['user'])
    data2 = parkinglot.objects.all()
    return render(re, 'user_dir/parking_lot_user_view.html',{'data':data,'data2':data2})

def buy_parking(re,id):
    if re.method == 'POST':
        user_details = parker.objects.get(email=re.session['user'])
        park_details = parkinglot.objects.get(pk=id)
        park_price = re.POST['price']
        no_hrs = re.POST['no_hrs']
        start_time = re.POST['start_time']
        end_time = re.POST['end_time']
        Email = re.POST['email']
        booked_date = re.POST['booked_date']
        data = parking_booking.objects.create(user_details=user_details, park_details=park_details, park_price=park_price, no_hrs=no_hrs, start_time=start_time, end_time=end_time, Email=Email, booked_date=booked_date)
        data.save()
        messages.success(re, 'Booked successfully')
        return redirect(user_booked_details)
    else:
        data=parkinglot.objects.get(pk=id)
        data1= parker.objects.get(email=re.session['user'])
        parking_lot = parkinglot.objects.get(pk=id)
        start_time = parking_lot.start_time
        end_time = parking_lot.end_time
        no_slots = parking_lot.no_slots
        time_range = range(start_time, end_time + 1)
        slots_range = range(no_slots)
        return render(re, 'user_dir/buy_parking.html', {'data': data,'data1':data1,'time_range': time_range, 'slots_range': slots_range})


def company_parking_user_view(re,id):
    data=parker.objects.get(email=re.session['user'])
    data1 = conv_parking.objects.filter(company_details=id)
    data2 =company.objects.get(pk=id)
    # Check if user has already booked on the same park_date
    user_bookings = conv_parking_booking.objects.filter(user_details=data, park_date__in=[park.park_date for park in data1])
    booked_dates = [booking.park_date for booking in user_bookings]
    return render(re,'user_dir/company_parking_user_view.html',{'data':data,'data1':data1,'data2':data2, 'booked_dates': booked_dates})



def buy_conv_parking(re,id):
    if re.method == 'POST':
        user_details = parker.objects.get(email=re.session['user'])
        park_details = conv_parking.objects.get(pk=id)
        Email = re.POST['email']
        phone_no = re.POST['phone']
        park_date = re.POST['park_date']
        no_slots = int(re.POST['stock'])    # Convert to int for comparison
        park_price = re.POST['price']
        if no_slots > park_details.stock_item:
            messages.error(re, f'Selected {no_slots} slots are unavailable, select less slots')
            return redirect(buy_conv_parking)
        if not Email:
            messages.error(re, 'Email cannot be blank')
            return redirect(buy_conv_parking)
            # Validate phone number (Indian format)
        phone_validator = RegexValidator(regex=r'^\d{10}$', message="Phone number must be entered in the format: '9896888739'. Up to 10 digits allowed.")
        try:
             phone_validator(phone_no)
        except ValidationError as phone_no:
            messages.error(re, str(phone_no))
            return redirect(buy_conv_parking)
        try:
            validate_email(Email)
        except ValidationError as Email:
            messages.error(re, str(Email))
            return redirect(buy_conv_parking)
        data = conv_parking_booking.objects.create(user_details=user_details, park_details=park_details, Email=Email,
                                                   phone_no=phone_no, park_date=park_date, no_slots=no_slots,
                                                   park_price=park_price)
        data.save()
        latest_booking = conv_parking_booking.objects.filter(user_details__email=re.session['user']).latest('id')
        s = latest_booking.no_slots
        am=park_details.stock_item -s
        conv_parking.objects.filter(pk=id).update(stock_item=am)
        messages.success(re, 'Booked successfully')
        return redirect('conv_parking_payment', total_price=park_price, Email=Email)
    else:
        data = conv_parking.objects.get(pk=id)
        data1= parker.objects.get(email=re.session['user'])
        data2 = conv_parking_booking.objects.filter(park_details=id)
        return render(re, 'user_dir/buy_conv_parking.html', {'data': data,'data1':data1,'data2':data2})

def conv_parking_payment(re,total_price,Email):
    latest_booking = conv_parking_booking.objects.filter(user_details__email=re.session['user']).latest('id')
    amount = latest_booking.park_price * 100
    order_currency = 'INR'
    client = razorpay.Client(auth=("rzp_test_SROSnyInFv81S4", "WIWYANkTTLg7iGbFgEbwj4BM"))
    payment = client.order.create({'amount': amount, 'currency': order_currency, 'payment_capture': '1'})
    latest_booking.park_price=total_price
    send_mail('Parking Booking',
              f'Hello, {latest_booking.user_details}. '
              f'You have successfully booked parking from {latest_booking.park_details}. '
              f'Park your vehicle on the date: {latest_booking.park_date}, you can park at any time at that day. '
              f'You can reply to this e-mail, by only using this {latest_booking.Email} e-mail address. '
              f'You have paid {latest_booking.park_price}₹/-.',
              'albinantonyappus@gmail.com', [Email],
              fail_silently=False)
    return render(re, "user_dir/payment.html", {'amount': amount})

def conv_booking_company_view(re, id):
    data = company.objects.get(c_email=re.session['c_id'])
    data1 = conv_parking_booking.objects.filter(park_details=id)
    return render(re, 'company/conv_booking_company_view.html', {'data': data,'data1': data1})

def user_conv_booked_details(re):
    data = parker.objects.get(email=re.session['user'])
    data1=conv_parking_booking.objects.filter(user_details=data)
    return render(re,'user_dir/user_conv_booked_details.html',{'data':data,'data1':data1})





