from django.db import models
from product.models import Product

# Create your models here.
class Purchase(models.Model):
    id = models.AutoField(primary_key=True)
    price = models.FloatField()
    date = models.DateTimeField()

class PurchaseProduct(models.Model):
    id = models.AutoField(primary_key=True)
    purchase = models.ForeignKey(Purchase, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    amount = models.IntegerField(default=1)
    