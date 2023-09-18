from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from Community.models import Community
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class MyUser(User):
    # id = models.AutoField(primary_key=True) có sẵn
    #first Name, last name, password, joined_date đã được kế thừa từ class user
    birth_year = models.DateField(auto_now_add=True)
    MetamarskID = models.CharField(max_length=255, blank=False, null=False)

    @receiver(post_save, sender=User)
    def create_user(sender, instance, created, **kwargs):
        if created:
            MyUser.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user(sender, instance, **kwargs):
        instance.myuser.save()

class UserHistory(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    update_date = models.DateField(auto_now_add=True)
    community_id = models.ForeignKey(Community, on_delete=models.CASCADE)
    content = models.CharField(max_length=255)
    def save(self, *args, **kwargs):
        # Get the day, month, and year from the created_date
        day = str(self.update_date.day).zfill(2)
        month = str(self.update_date.month).zfill(2)
        year = str(self.update_date.year % 100).zfill(2)

        # Concatenate community_id and formatted created_date to generate commu_history_id
        self.id = f"{self.user_id}-{self.community_id}-{day}{month}{year}"

        super().save(*args, **kwargs)


class UserCommunity(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    community_id = models.ForeignKey(Community, on_delete=models.CASCADE)
    score = models.IntegerField()
    joined_date = models.DateField(auto_now_add=True)
    def save(self, *args, **kwargs):
        # Get the day, month, and year from the created_date
        day = str(self.joined_date.day).zfill(2)
        month = str(self.joined_date.month).zfill(2)
        year = str(self.joined_date.year % 100).zfill(2)

        # Concatenate community_id and formatted created_date to generate commu_history_id
        self.id = f"{self.user_id}-{self.community_id}-{day}{month}{year}"

        super().save(*args, **kwargs)
