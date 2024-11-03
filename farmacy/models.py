from django.db import models
from . createQR import qr_creation
from django.core.files import File
from io import BytesIO
import os


class Pharmacy(models.Model):
    phone_number = models.CharField(max_length=10,unique=True)
    pharmacy_name = models.CharField(max_length=20)
    license_number = models.CharField(max_length=6, unique=True)
    qr_code = models.ImageField(upload_to='qrcodes/', blank=True, null=True)

    def __str__(self):
        return self.pharmacy_name
    
    def save(self, *args, **kwargs):
        if not self.qr_code:
            data = f"Pharmacy: {self.pharmacy_name}, Phone: {self.phone_number}, License: {self.license_number}"
            img = qr_creation(data)
            buffer = BytesIO()
            img.save(buffer, format="PNG")
            buffer.seek(0)
            self.qr_code.save(f"{self.pharmacy_name}_qr.png", File(buffer), save=False)

        super().save(*args, **kwargs)

