from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class CustomUser(AbstractUser):
    date_of_birth = models.DateField(blank=True,null=True)
    profile_pic = models.ImageField(upload_to='images/',blank=True)
    about = models.CharField(max_length=10000)