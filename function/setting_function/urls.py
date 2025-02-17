from django.urls import path

from . import views
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth_views #input this auth_view to have have option to logout




urlpatterns = [
    path('background-setting/', views.background_color_form_views, name='background_color_form_views'),
]
