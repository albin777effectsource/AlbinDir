from django.urls import path
from.import views
#about contact feature price service quote team testimonial
urlpatterns = [
    path('', views.index),
    path('index', views.index),
    path('dark_index', views.dark_index),

    path('about.html', views.about),
    path('contact.html', views.contact),
    path('feature.html', views.feature),
    path('service.html', views.service),
    path('quote.html', views.quote),
    path('team.html', views.team),
    path('register', views.register),
    path('login', views.login),
    path('e404', views.e404),
    path('user_index', views.user_index),
    path('parking_lot_user_view', views.parking_lot_user_view),
    path('user_conv_parking_view', views.user_conv_parking_view),

    path('admin_index', views.admin_index),
    path('company_register', views.company_register),
    # path('company_login', views.company_login),
    path('company_index', views.company_index),
    path('disp_user', views.disp_user),
    path('staff_register', views.staff_register),
    path('disp_staff_details', views.disp_staff_details),
    path('disp_park2', views.disp_park2),
    # path('staff_login', views.staff_login),
    path('staff_index', views.staff_index),
    path('our_staff', views.our_staff),
    path('park_book/<id>', views.park_book),
    # path('delete/<id>', views.delete),
    path('company_admin_edit/<id>', views.company_admin_edit),
    path('company_edit/<id>', views.company_edit, name='company_edit'),

    path('add_parking_lot', views.add_parking_lot),
    path('add_conv_parking', views.add_conv_parking),
    path('conv_parking_company_view', views.conv_parking_company_view),

    path('delete_conv_parking_by_company/<id>', views.delete_conv_parking_by_company),
    path('company_parking_user_view/<id>', views.company_parking_user_view),

    # path('buy_parking/<id>', views.buy_parking),#parking_booking
    path('buy_parking/<int:id>/', views.buy_parking, name='buy_parking'),

    path('success', views.success),

    path('company_parking_user_view/buy_conv_parking/<id>/', views.buy_conv_parking, name='buy_conv_parking'),
    path('conv_parking_payment/<total_price>/<Email>/', views.conv_parking_payment, name='conv_parking_payment'),

    path('user_booked_details', views.user_booked_details),
    path('user_conv_booked_details', views.user_conv_booked_details),

    path('parking_lot_company_view', views.parking_lot_company_view),
    path('user_admin_edit/<id>', views.user_admin_edit),#user_profile_edit
    path('user_profile_edit/<id>', views.user_profile_edit),
    path('staff_company_edit/<id>', views.staff_company_edit),
    path('staff_admin_edit/<id>', views.staff_admin_edit),
    path('parking_lot_company_edit/<id>', views.parking_lot_company_edit),
    path('staff_edit/<id>', views.staff_edit),
    path('parking_lot_staff_view', views.parking_lot_staff_view),
    path('delete_staff_by_company/<id>', views.delete_staff_by_company),
    path('delete_company_by_admin/<id>', views.delete_company_by_admin),
    path('delete_staff_by_admin/<id>', views.delete_staff_by_admin),
    path('delete_user_by_admin/<id>', views.delete_user_by_admin),
    path('delete_parking_lot_by_company/<id>', views.delete_parking_lot_by_company),
    path('company_user_view/<id>', views.company_user_view),
    path('company_outsider_view/<id>', views.company_outsider_view),
    path('cancel_booking_by_user/<id>', views.cancel_booking_by_user),
    path('parkinglot_admin_view', views.parkinglot_admin_view),
    path('parking_booking_admin_view/<id>', views.parking_booking_admin_view),
    path('parking_booking_user_view/<id>', views.parking_booking_user_view),

    path('all_parking_booking_admin_view', views.all_parking_booking_admin_view),
    path('booking_company_view/<id>', views.booking_company_view),

    path('conv_booking_company_view/<id>', views.conv_booking_company_view),

    path('parking_booking_staff_view/<id>', views.parking_booking_staff_view),
    path('company_settings', views.company_settings),


]