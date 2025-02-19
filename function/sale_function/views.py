from django.shortcuts import render
from django.contrib.auth import authenticate,login
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from .models import TransactionDetail
from django.db.models import Prefetch

from .models import Product
from .forms import ProductInputForm

from django.http import HttpResponseRedirect
from django.views import View


@login_required
def gym_sale_views(request):
    # Use select_related for ForeignKey relationships and prefetch_related for reverse ForeignKey relationships
    sales = TransactionDetail.objects.select_related('order').prefetch_related('order__orderitem_set__product')
    return render(request, 'sale_gym.html', {'sales': sales})


#def order_sale_view(request):
    


class ProductInputView(View):
    template_name = 'input_product.html'

    def get(self, request):
        # Retrieve all products and render them with the form
        products = Product.objects.all()
        form = ProductInputForm()
        return render(request, self.template_name, {'products': products, 'form': form})

    def post(self, request):
        # Handle form submission
        form = ProductInputForm(request.POST)
        products = Product.objects.all()

        if form.is_valid():
            form.save()
            return redirect('product_input_views')  # Replace with the appropriate URL name

        return render(request, self.template_name, {'form': form, 'products': products})