from django.db import models
from datetime import date,timedelta
from django.db.models import F #2/5/2025 for item to address the stock








class GymEquipment(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    stock = models.IntegerField()
    picture =models.ImageField(upload_to='equipment-picture/', null=True, blank=True)

    class Meta:
        db_table = 'gym_equipment_record'


