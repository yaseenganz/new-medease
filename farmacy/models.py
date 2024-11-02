from django.db import models
import qrcode
from django.core.files.base import ContentFile
import uuid


class Pharmacy(models.Model):
    name = models.CharField(max_length=255)
    address = models.TextField()
    contact_number = models.CharField(max_length=15)
    unique_code = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    qr_code = models.ImageField(upload_to='qr_codes/', blank=True, null=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.generate_qr_code()

    def generate_qr_code(self):
        # Generate QR Code
        qr = qrcode.QRCode(version=1, box_size=10, border=5)
        qr.add_data(str(self.unique_code))  # You can add a URL or other data if needed
        qr.make(fit=True)

        # Create an image file
        img = qr.make_image(fill_color="black", back_color="white")

        # Save the QR code image to the model field
        img_content = ContentFile(img.tobytes())
        self.qr_code.save(f'{self.unique_code}.png', img_content, save=False)  # save=False because we're already calling save() above
        self.save()

    def __str__(self):
        return self.name


class Pharmacy(models.Model):
    phone_number = models.CharField(max_length=10,unique=True)
    pharmacy_name = models.CharField(max_length=20)
    license_number = models.CharField(max_length=6, unique=True)

    def __str__(self):
        return self.pharmacy_name
    
