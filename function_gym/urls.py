from django.urls import path

from . import views
from django.conf.urls.static import static
from django.conf import settings



urlpatterns =[
    path('',views.dash_board_views,name='dash_board_views'),
    path('member-list',views.member_views,name='member_views')

 
]
if settings.DEBUG:
        urlpatterns += static(settings.STATIC_URL, document_root=settings.MEDIA_ROOT)