from django.db import models

class GymMember(models.Model):



    GENDER_CHOICES =  [
        ('Male','Male'),

        ('Female','Female')
        ]


    id_card = models.CharField(max_length=50, unique=True)
    expiry = models.DateField()
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    phone_number = models.CharField(max_length=15)
    address = models.TextField()
    profile_image = models.ImageField(upload_to='images/', null=True, blank=True)

    class Meta:
        db_table = 'gym_members'  # Custom table name
      

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.id_card})"
    
class GymSale(models.Model):
    
     
    id_card = models.CharField(max_length=50, unique=True)                
    sale_date = models.DateField()           
    payment_method = models.CharField(max_length=100)  
    sale_price = models.IntegerField()
    item = models.CharField(max_length=100)

    class Meta:
        db_table = 'sale_table'  # Custom table name



class LoginRecord(models.Model):
    id_card = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    login_time = models.CharField(max_length=100)
    login_date = models.CharField(max_length=100)


    def __str__(self):
        return f'{self.id_card}-{self.first_name} {self.last_name} - {self.login_time}'

    class Meta:
        db_table = 'gym_login_record'
        unique_together = ('id_card', 'login_date')


class GymEquipment(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    profile_picture =models.ImageField(upload_to='equipment-picture/', null=True, blank=True)

    class Meta:
        db_table = 'equipment'
