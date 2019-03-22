from django.db import models
from products.models import Product
from stores.models import Store
# Create your models here.
class Inventory(models.Model):
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    product =  models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)

    def __str__(self):
        return '{}-{}-{}'.format(self.store.name,self.product.name,self.quantity)