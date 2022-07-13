from django.db import models

# Create your models here.
class saving(models.Model):
    ac_no = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    ifsc = models.CharField(max_length=20)
    balance = models.IntegerField()


class current(models.Model):
    ac_no = models.BigIntegerField(primary_key=True)
    businessname = models.CharField(max_length=50)
    ifsc = models.CharField(max_length=20)
    balance = models.IntegerField()

class fixed_deposit(models.Model):
    ac_no = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    deposit_date = models.DateField()
    maturity_date = models.DateField()
    interest = models.IntegerField()
    maturity_ammount = models.IntegerField()

'''class contactus(models.Model):
    name = models.CharField(max_length=30,label='Enter Your name')
    email = models.EmailField(label='Enter Your name')
    message = models.TextField(max_length=100 ,label='Your Message',required=True)
'''