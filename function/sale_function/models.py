from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

class OrderDetail(models.Model):
    items = models.ManyToManyField(Product, through='OrderItem', related_name='order_details')

    def __str__(self):
        return f"Order {self.id}"

class OrderItem(models.Model):
    order = models.ForeignKey(OrderDetail, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    total = models.DecimalField(max_digits=10, decimal_places=2, editable=False)

    def save(self, *args, **kwargs):
        self.total = self.product.price * self.quantity
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.product.name} x {self.quantity}"

class TransactionDetail(models.Model):
    order = models.OneToOneField(OrderDetail, on_delete=models.CASCADE)
    payment_method = models.CharField(max_length=100)
    trasaction_date = models.DateField(auto_created=True)
    total_payment = models.DecimalField(max_digits=10, decimal_places=2, editable=False)

    class Meta:
        db_table ='sale_table'

    def save(self, *args, **kwargs):
        self.total_payment = sum(item.total for item in self.order.orderitem_set.all())
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Transaction {self.id}"
