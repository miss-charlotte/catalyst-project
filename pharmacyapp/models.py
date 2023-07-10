from django.db import models
from django.contrib.auth.models import User
import datetime

d = datetime.date.today()

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length = 50, null = True, blank = True)
    def __str__(self):
        return self.name
    
class Product(models.Model):
    categoryName = models.ForeignKey(Category, on_delete= models.CASCADE, null = True, blank = True)

    medicineName = models.CharField(max_length =50, null =True, blank =True)
    quantityinStore = models.IntegerField(default=0)
    receivedQuantity = models.IntegerField(default=0)
    quantitySold = models.IntegerField(default =0)
    cost = models.IntegerField(default =0)
    expiredQuantity = models.IntegerField(default =0)
    unitCost = models.IntegerField(default =0)
    expiryDate = models.DateField(null=True, blank=True)

    @property
    def expiredQuantity(self):
        if self.expiryDate < datetime.date.today():
            return self.quantityinStore
        else:
            return 0

    def __str__(self):
        return self.medicineName 
    

class Sale(models.Model):
    medicine = models.ForeignKey(Product, on_delete=models.CASCADE)

    quantity = models.IntegerField(default = 0) 
    amountPaid = models.IntegerField(default = 0)
    boughtBy = models.CharField(max_length = 50, null =True, blank = True)
    unitCost = models.IntegerField(default = 0)
    date = models.DateField(auto_now=True)

    def getTotal(self):
        total = self.quantity * self.medicine.unitCost
        return int(total)
    
    def getChange(self):
        change = self.getTotal() - self.amountPaid
        return abs(int(change))

    def __str__(self):
        return self.medicine.medicineName
