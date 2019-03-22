from django.db import models

# Create your models here.
class Store(models.Model):
    name =  models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    capacity = models.PositiveIntegerField(blank=True, null=True)

    def __str__(self):
        return '{} - {}'.format(self.name, self.location)