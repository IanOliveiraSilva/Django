from django.db import models

# Create your models here.


class AddStock(models.Model):
    productsName = models.CharField(max_length=100, blank=False) 
    productsCategory = models.CharField(max_length=20, blank=False)
    productsQuantity = models.IntegerField(blank=False)
    productsPrice = models.FloatField(blank=False)


    def __str__(self):
        return self.title