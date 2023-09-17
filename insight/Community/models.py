from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Community(models.Model):
    # khóa đại diện , khóa chính
    id = models.AutoField(primary_key=True) 
    name = models.CharField(max_length=255, blank=True, null=True)
    created_date = models.DateField(auto_now_add=True, blank=True, null=True)
    created_user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.CharField(max_length=255, blank=True, null=True)

    # print(str(abcd))
    def __str__(self):
        return str(self.name) + '-' + str(self.created_user)
    
    def get_absolute_url(selft):
        return reverse('home')
