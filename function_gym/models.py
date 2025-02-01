from django.db import models
from datetime import date,timedelta

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
    join_date = models.DateField(auto_now_add=True) # it will auto add the date now 
    renewed = models.BooleanField(default=False)
    profile_image = models.ImageField(upload_to='images/')

    class Meta:
        db_table = 'gym_members'  # Custom table name
      
    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.id_card})"
    
    def save(self,*args,**kwargs):
        today = date.today()
        if self.expiry > today + timedelta(days=20):
           self.renewed = True
        else:
            self.renewed = False
        super().save(*args,**kwargs)    
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
    stock = models.IntegerField()
    picture =models.ImageField(upload_to='equipment-picture/', null=True, blank=True)

    class Meta:
        db_table = 'gym_equipment_record'

class SettingColorTable(models.Model):
  
    name = models.CharField(max_length=100)
    value = models.CharField(max_length=100)
    active = models.BooleanField()  # Whether this color is active
    

    class Meta: 
        db_table = 'setting_color_table'

    def __str__(self):
        # Return "Active" or "Deactive" based on the `active` field
        return f"{self.name} - {'Active' if self.active else 'Deactive'}"
        

class SettingFontTable(models.Model):
    name  = models.CharField(max_length=100)
    value = models.CharField(max_length=100)
    active = models.BooleanField()


    class Meta:
        db_table = 'setting_font_table'

    def __str__(self):
        return f'{self.name} - {'Active' if self.active else 'Deactive'}'