from django.db import models

# Create your models here.

class Membership(models.Model):
    member_id =models.IntegerField()
    first_name= models.CharField(max_length =64)
    last_name = models.CharField(max_length = 64)
    phone_number = models.IntegerField()
    email_address =models.EmailField()
    address = models.CharField(max_length = 255)

