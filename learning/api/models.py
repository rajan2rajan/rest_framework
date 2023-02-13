from django.db import models

Bloodgroup = [
    ("A+", "A+"), 
    ("A-", "A-"), 
    ("B+", "B+"), 
    ("B-", "B-"), 
    ("AB-", "AB-"),
    ("AB+", "AB+"),
    ("O-", "O-"),
    ("O+", "O+"),
]

Gender =[
    ("M","M"),("F","F"),("O","O")
]

# this model is for reciver people 
class Database(models.Model):
    firstname           =models.CharField(max_length=100)
    middlename          =models.CharField(max_length=100,blank=True)
    lastname            =models.CharField(max_length=100)
    age                 =models.IntegerField()
    contactnumber       =models.IntegerField()
    incident            =models.CharField(max_length=100)
    bloodgroup          =models.CharField(max_length=10,choices=Bloodgroup)
    Gender              =models.CharField(max_length=1,choices=Gender)
    location            =models.CharField(max_length=100)
    unit                =models.PositiveIntegerField()
    emergency           =models.BooleanField()
    requiredate         =models.CharField(max_length=100)