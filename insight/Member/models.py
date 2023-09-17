from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
# class MyUser(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='myuser')
#     MetamarskID = models.CharField(max_length=255, blank=False, null=False)

#     @receiver(post_save, sender=User)
#     def create_user(sender, instance, created, **kwargs):
#         if created:
#             MyUser.objects.create(user=instance)

#     @receiver(post_save, sender=User)
#     def save_user(sender, instance, **kwargs):
#         instance.myuser.save()
