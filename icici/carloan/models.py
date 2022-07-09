from django.db import models

# Create your models here.
class employee(models.Model):
    name  = models.CharField(max_length=30)
    city = models.CharField(max_length=20)
    mobile = models.BigIntegerField()

class client(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(primary_key=True)
    company = models.CharField(max_length=30)

