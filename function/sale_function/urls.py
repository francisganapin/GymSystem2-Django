from django.urls import path

from . import views
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth_views #input this auth_view to have have option to logout




urlpatterns = [
    path('sale-dashboard/', views.gym_sale_views, name='gym_sale_views'),
    path('input-product/',views.ProductInputView.as_view(),name='product_input_views')
]
