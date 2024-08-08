from django.db import models

# Create your models here.
class ContactDB(models.Model):
    YourName = models.CharField(max_length=100,null=True,blank=True)
    Email = models.EmailField(max_length=100, null=True, blank=True)
    Subject = models.CharField(max_length=100, null=True, blank=True)
    Message = models.CharField(max_length=100, null=True, blank=True)

# class ServicePackage(models.Model):
#     name = models.CharField(max_length=100)
#     price = models.DecimalField(max_digits=10, decimal_places=2)
#     description = models.TextField()
#     is_active = models.BooleanField(default=False)  # For highlighting the active package
#
#     def __str__(self):
#         return self.name
class CartDb(models.Model):
    Username = models.CharField(max_length=100, null=True, blank=True)
    Servicename = models.CharField(max_length=100, null=True, blank=True)
    Quantity = models.IntegerField(null=True, blank=True)
    Price = models.IntegerField(null=True, blank=True)

class RegisterDb(models.Model):
    Username = models.CharField(max_length=100, null=True, blank=True)
    Email = models.EmailField(max_length=100, null=True, blank=True)
    Password = models.CharField(max_length=100, null=True, blank=True)

class OrderDb(models.Model):
    Name = models.CharField(max_length=100, null=True, blank=True)
    Address = models.CharField(max_length=100, null=True, blank=True)
    Phone = models.IntegerField(null=True, blank=True)
    EmailAddress = models.EmailField(max_length=100, null=True, blank=True)
    Total = models.IntegerField(null=True, blank=True)