from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class user_profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)

    #additional fields
    phone = models.BigIntegerField()

    age = models.PositiveIntegerField()

    address = models.CharField(max_length=100)
    
    user_img = models.ImageField(upload_to='userimg',blank=True,null=True)