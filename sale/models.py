from django.db import models
from product.models import Product

# Create your models here.
class Sale(models.Model):
    id = models.AutoField(primary_key=True)
    price = models.FloatField()
    date = models.DateTimeField(auto_now_add=True)

class SaleProduct(models.Model):
    id = models.AutoField(primary_key=True)
    sale = models.ForeignKey(Sale, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    amount = models.IntegerField(default=1)
    