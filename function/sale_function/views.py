from django.shortcuts import render
from django.contrib.auth import authenticate,login
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from .models import TransactionDetail
from django.db.models import Prefetch



@login_required
def gym_sale_views(request):
    # Use select_related for ForeignKey relationships and prefetch_related for reverse ForeignKey relationships
    sales = TransactionDetail.objects.select_related('order').prefetch_related('order__orderitem_set__product')
    return render(request, 'sale_gym.html', {'sales': sales})
