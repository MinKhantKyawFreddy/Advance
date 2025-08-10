from django.db import models

# Create your models here.
class Member(models.Model):
    First_Name = models.CharField(max_length=255)
    Last_Name = models.CharField(max_length=255)
    Email = models.EmailField(max_length=255)
    Phone = models.CharField(max_length=20)

class Booking(models.Model):
    TIME_SLOTS = [
        ("09:00-10:00", "09:00 - 10:00"),
        ("10:00-11:00", "10:00 - 11:00"),
        ("11:00-12:00", "11:00 - 12:00"),
        ("12:00-13:00", "12:00 - 13:00"),
        ("13:00-14:00", "13:00 - 14:00"),
        ("14:00-15:00", "14:00 - 15:00"),
        ("15:00-16:00", "15:00 - 16:00"),
        ("16:00-17:00", "16:00 - 17:00"),
        ("17:00-18:00", "17:00 - 18:00"),
    ]

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    time_slot = models.CharField(max_length=20, choices=TIME_SLOTS)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.time_slot}"