from django.db.models.signals import post_migrate
from django.dispatch import receiver
from .models import GymMember
from django.apps import apps

@receiver(post_migrate)
def create_default_settings(sender,**kwargs):
    if sender.name != 'member_function':
        return
    
    GymMember = apps.get_model('member_function','GymMember')

    gym_members =[
        {
        'id_card':'well-2025BF',
         'expiry':'2026-11-11',
         'first_name':'firs_well',
         'last_name':'last_well',
         'gender':'female',
         'phone_number':'0912345671',
         'address':'address_well',
         'join_date':'2025-1-25',
         'renewed':0,
         'profile_image':'profile',
         }
    ]

    for data in gym_members:
        GymMember.objects.get_or_create(
            id_card=data['id_card'],
            defaults=data
        )


