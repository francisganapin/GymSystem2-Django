from django.urls import path

from . import views
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth_views #input this auth_view to have have option to logout




urlpatterns = [
    path('', views.dash_board_views, name='dash_board_views'),

 

    path('sale-dashboard/', views.gym_sale_views, name='gym_sale_views'),
    path('login-record-dashboard/', views.login_record_views, name='login_record_views'),
    
    path('equipment-record-list/', views.equipment_record_views, name='equipment_record_views'),
    path('equipment-record-list/detail/<int:equipment_id>', views.equipment_record_detail_views, name='equipment_record_detail_views'),
    path('background-setting/', views.background_color_form_views, name='background_color_form_views'),


    path('user-login/', views.user_login, name='user_login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout') # input this one if you want to logout the user



]
