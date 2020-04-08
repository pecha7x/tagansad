from django.db import models


class PlantKind(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Plant(models.Model):
    kind = models.ForeignKey(PlantKind, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    description = models.TextField(default='')
    purchase_price = models.DecimalField(max_digits=10, decimal_places=2)
    buyer_price = models.DecimalField(max_digits=10, decimal_places=2)
    max_discount = models.IntegerField()

    def __str__(self):
        return self.name
