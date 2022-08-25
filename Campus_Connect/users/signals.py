from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from . models import profile

@receiver(post_save, sender=User)
def create_profile(sender, created, instance , **kwargs):
    if created:
        profile.objects.create(user=instance)
    instance.profile.save()
        # print('Profile Created') 

@receiver(post_save, sender=User)
def update_profile(sender, instance, created, **kwargs):
    if created == False:
        instance.profile.save()
        # print('profile updated')