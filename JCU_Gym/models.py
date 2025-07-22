from django.db import models

# Create your models here.
class Member(models.Model):
    First_Name = models.CharField(max_length=255)
    Last_Name = models.CharField(max_length=255)
    Email = models.EmailField(max_length=255)
    Phone = models.CharField(max_length=20)