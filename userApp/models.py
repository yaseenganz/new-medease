from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=10,unique=True)
    full_name = models.CharField(max_length=20)
    def str(self):
        return self.full_name
    
    

class PatientModel(models.Model):
    user=models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    GENDER_CHOICES = (('f','Female'),('m',"Male"))
    gender = models.CharField(choices=GENDER_CHOICES,max_length=1)


    def str(self):
        return self.user.username
    

class Priscription(models.Model):
    pass