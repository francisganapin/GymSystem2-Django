from django.db import models

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