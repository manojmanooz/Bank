from django.db import models

class Details(models.Model):
    name=models.CharField(max_length=100)
    date=models.DateField(auto_now=True)
    email=models.EmailField(blank=True)
    phone=models.IntegerField()
    age=models.IntegerField()
    male=models.BooleanField(default=None)
    female=models.BooleanField(default=None)
    district=models.CharField(max_length=100)
    branch=models.CharField(max_length=100)
    address=models.TextField()
    credit=models.BooleanField(default=None)
    debit=models.BooleanField(default=None)
    cheque=models.BooleanField(default=None)