from django.urls import path

from . import views
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth_views




urlpatterns = [


    path('member-list/', views.member_views, name='member_views'),
    path('member-list/update/<int:member_id>', views.member_update_views, name='member_update_views'),

    path('member-login/', views.member_login, name='member_login'),
    path('member-register/', views.member_register, name='member_register'),
    path('member-register/successfull/<int:member_id>', views.member_register_successful_views, name='member_register_successful_views'),
  

]
