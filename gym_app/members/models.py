from django.db import models

class Member(models.Model):
  firstname = models.CharField(max_length=255)
  email = models.CharField(max_length=255)
  student_id = models.IntegerField(null=True)
  password = models.CharField(max_length=128)