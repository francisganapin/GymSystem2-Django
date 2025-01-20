from django.urls import path

from . import views
from django.conf.urls.static import static
from django.conf import settings



urlpatterns =[
    path('',views.dash_board_views,name='dash_board_views'),
    path('member-list',views.member_views,name='member_views'),
    path('member-login',views.member_login,name='member_login'),
    path('member-register',views.member_register,name='member_register'),
    path('sale-dashboard',views.gym_sale_views,name='gym_sale_views'),
    path('login-record-dashboard',views.login_record_views,name='login_record_views')

 
]
if settings.DEBUG:
        urlpatterns += static(settings.STATIC_URL, document_root=settings.MEDIA_ROOT)