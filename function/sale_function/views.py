from django.shortcuts import render
from django.contrib.auth import authenticate,login
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from .models import TransactionDetail
from django.db.models import Prefetch

from .models import Product,OrderDetail,OrderItem
from .forms import *

from django.forms import inlineformset_factory

from django.views import View




@login_required
def gym_sale_views(request):
    # Use select_related for ForeignKey relationships and prefetch_related for reverse ForeignKey relationships
    sales = TransactionDetail.objects.select_related('order').prefetch_related('order__orderitem_set__product')
    return render(request, 'sale_gym.html', {'sales': sales})


#def order_sale_view(request):
    

class ProductInputView(View):
    template_name = 'input_product.html'

    def get_products(self, request):
        products = Product.objects.all()
        paginator = Paginator(products, 5)
        page_number = request.GET.get('page')
        return paginator.get_page(page_number)

    def get(self, request):
        products = self.get_products(request)
        form = ProductInputForm()
        return render(request, self.template_name, {'products': products, 'form': form})

    def post(self, request):
        products = self.get_products(request)

        # Handle product input (Add new product)
        if 'add_product' in request.POST: 
            form = ProductInputForm(request.POST) 
            if form.is_valid():
                form.save()
                return redirect('product_input_views')
            return render(request, self.template_name, {'form': form, 'products': products})

        # Handle stock update
        elif 'update_product' in request.POST:
            return self.update_product_field(request, 'stock', products)

        # Handle price update
        elif 'update_product' in request.POST:
            return self.update_product_field(request, 'price', products)

        # Default fallback
        return render(request, self.template_name, {'products': products, 'message': 'Invalid action.'})

    def update_product_field(self, request, field, products):
        product_id = request.POST.get('id')
        value = request.POST.get(field)

        try:
            product = Product.objects.get(id=product_id)
            setattr(product, field, value)  # Dynamically set 'stock' or 'price'
            product.save()
            message = f"{field.capitalize()} updated successfully!"
            
        except Product.DoesNotExist:
            message = "Product not found."
        except Exception as e:
            message = f"Error: {str(e)}"

        return render(request, self.template_name, {'products': products, 'message': message})



