from django.db import models

class GymMember(models.Model):
    id_card = models.CharField(max_length=50, unique=True)
    expiry = models.DateField()
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=10)
    phone_number = models.CharField(max_length=15)
    address = models.TextField()
    profile_image = models.ImageField(upload_to='profile_image/', null=True, blank=True)

    class Meta:
        db_table = 'gym_members'  # Custom table name


class GymSale(models.Model):
    
     
    id_card = models.CharField(max_length=50, unique=True)                
    sale_date = models.DateField()           
    payment_method = models.CharField(max_length=100)  
    sale_price = models.IntegerField()
    expiry = models.DateField()

    class Meta:
        db_table = 'sale_table'  # Custom table name