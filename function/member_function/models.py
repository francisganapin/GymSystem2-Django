from django.db import models
from datetime import datetime, date, timedelta
from django.db.models import F #2/5/2025 for item to address the stock

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
    
    def save(self, *args, **kwargs):
        today = date.today()
        
        # Ensure self.expiry is a datetime.date object
        if isinstance(self.expiry, str):
            self.expiry = datetime.strptime(self.expiry, '%Y-%m-%d').date()
        
        if self.expiry > today + timedelta(days=20):
            self.renewed = True
        else:
            self.renewed = False
        
        super().save(*args, **kwargs)
        




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