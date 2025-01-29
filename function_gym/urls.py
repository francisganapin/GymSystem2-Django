from django.urls import path

from . import views
from django.conf.urls.static import static
from django.conf import settings



urlpatterns =[
    path('',views.dash_board_views,name='dash_board_views'),
    path('member-list',views.member_views,name='member_views'),
    path('member-login',views.member_login,name='member_login'),
    path('member-register',views.member_register,name='member_register'),
    path('member-register/successfull/<int:member_id>',views.member_register_successful_views,name='member_register_successful_views'),
    path('sale-dashboard',views.gym_sale_views,name='gym_sale_views'),
    path('login-record-dashboard',views.login_record_views,name='login_record_views'),
    path('member-list/update/<int:member_id>',views.member_update_views,name='member_update_views'),
    path('equipment-record-list',views.equipment_record_views,name='equipment_record_views'),

    # this will be the form so that we can changes the background color of our django
    path('background-setting',views.background_color_form_views,name='background_color_form_views')
 
]
