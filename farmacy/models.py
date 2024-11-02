from django.db import models


class Pharmacy(models.Model):
    phone_number = models.CharField(max_length=10,unique=True)
    pharmacy_name = models.CharField(max_length=20)
    license_number = models.CharField(max_length=6, unique=True)

    def __str__(self):
        return self.pharmacy_name
    
