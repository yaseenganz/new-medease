# from django.db import models
# from hospital.models import HospitalModel 
# from userApp.models import CustomUser


# class PatientDetails(models.Model):
#     name = models.CharField(max_length=100)
#     age = models.IntegerField()

#     GENDER_CHOICES = [
#         ('male', 'Male'),
#         ('female', 'Female'),
#         ('other', 'Other'),
#     ]

#     gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
#     hospital = models.ForeignKey(HospitalModel, on_delete=models.CASCADE)
#     token_number = models.PositiveIntegerField(editable=False, unique=True)

#     def save(self, *args, **kwargs):
#         if not self.token_number:  
#             last_token = PatientDetails.objects.order_by('-token_number').first()
#             self.token_number = last_token.token_number + 1 if last_token else 1
#         super().save(*args, **kwargs)

#     def __str__(self):
#         return self.name
