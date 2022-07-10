from django.db import models

# Create your models here.

class credit(models.Model):
    card_no = models.IntegerField(primary_key=True)
    card_name = models.CharField(max_length=30)
    card_expiry = models.DateField()


class fast_tag(models.Model):
    name = models.CharField(max_length=30)
    vehicle_no= models.CharField(max_length=30)
    registered_bank = models.CharField(max_length=30)
    address = models.CharField(max_length=20)

