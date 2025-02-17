from django.db.models.signals import post_migrate
from django.dispatch import receiver
from django.apps import apps

@receiver(post_migrate)
def create_default_setting(sender, **kwargs):
    if sender.name != 'function.setting_function':
        return
    
    SettingColorTable = apps.get_model('setting_function', 'SettingColorTable')
    SettingFontTable = apps.get_model('setting_function', 'SettingFontTable')

    color_defaults = [
        {'name': 'Sky Blue', 'value': "#3498db", 'active': True},
        {'name': 'Emerald', 'value': "#2ecc71", 'active': False},
        {'name': 'Sunset Orange', 'value': "#e67e22", 'active': False},
        {'name': 'Amethyst', 'value': "#9b59b6", 'active': False},
        {'name': 'Turquoise', 'value': "#1abc9c", 'active': False},
        {'name': 'Midnight Blue', 'value': "#2c3e50", 'active': False},
        {'name': 'Concrete', 'value': "#95a5a6", 'active': False},
        {'name': 'Alizarin', 'value': "#e74c3c", 'active': False},
        {'name': 'Carrot', 'value': "#e67e22", 'active': False},
    ]

    font_defaults = [
        {"name": "Default Font", "value": "Arial", "active": True},
        {"name": "Heading Font", "value": "Roboto", "active": False},
        {"name": "Body Font", "value": "Times New Roman", "active": False},
        {"name": "Title Font", "value": "Helvetica", "active": False},
        {"name": "Subtitle Font", "value": "Courier New", "active": False},
        {"name": "Caption Font", "value": "Verdana", "active": False},
        {"name": "Menu Font", "value": "Tahoma", "active": False},
        {"name": "Button Font", "value": "Georgia", "active": False},
        {"name": "Label Font", "value": "Comic Sans MS", "active": False},
    ]

    
    for data_color in color_defaults:
            SettingColorTable.objects.get_or_create(
                value=data_color['value'],
                defaults={
                    'name':data_color['name'],
                    'active':data_color['active']
                }
            )


  
    for data_font in font_defaults:
        SettingFontTable.objects.get_or_create(
            value=data_font['value'],
            defaults={
                    'name':data_font['name'],
                    'active':data_font['active']
                }
            )
