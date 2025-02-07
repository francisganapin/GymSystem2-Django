from django.db import models
from datetime import date,timedelta
from django.db.models import F #2/5/2025 for item to address the stock



class GymSale(models.Model):
    sale_date = models.DateField()
    payment_method = models.CharField(max_length=100)
    total_sale = models.IntegerField(default=0)  # Default to zero

    class Meta:
        db_table = 'sale_table'

    def save(self, *args, **kwargs):
        # Ensure the GymSale instance is saved first before calculating total
        super().save(*args, **kwargs)

        # Now calculate total_sale based on SaleItems linked to this GymSale
        self.total_sale = sum(item.get_total_price() for item in self.sale_items.all())
        GymSale.objects.filter(id=self.id).update(total_sale=self.total_sale)






        




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