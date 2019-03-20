from django.db import models

UOM = (
    ('KG', 'Kilogram'),
    ('UNIT','Unit'),
    ('PKT','Packets'),
)
class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.PositiveIntegerField()
    uom = models.CharField(max_length=255, choices=UOM, default='UNIT')

    def str(self):
        return '{} - {}'.format(self.name, self.price)