from django.db import models


# Create your models here.
class Record(models.Model):
    creation_date=models.DateTimeField(auto_now_add=True)
    first_name=models.CharField(max_length=100)
    email=models.EmailField(max_length=255)
    phone=models.CharField(max_length=30)
    address=models.TextField(max_length=300)
    city=models.CharField(max_length=255)
    Province=models.CharField(max_length=255)
    country=models.CharField(max_length=255)
    def __str__(self):
        return self.first_name



