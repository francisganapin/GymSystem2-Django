from django.urls import path

from . import views
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth_views #input this auth_view to have have option to logout




urlpatterns = [
    path('', views.dash_board_views, name='dash_board_views'),

 


    
    path('equipment-record-list/', views.equipment_record_views, name='equipment_record_views'),
    path('equipment-record-list/detail/<int:equipment_id>', views.equipment_record_detail_views, name='equipment_record_detail_views'),
    path('user-login/', views.user_login, name='user_login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout') # input this one if you want to logout the user



]
