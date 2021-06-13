from django.db import models

# Create your models here.


class CryptoData(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)
    image = models.URLField(blank=True, null=True)
    price = models.CharField(max_length=100, blank=True, null=True)
    rank = models.CharField(max_length=10, blank=True, null=True)
    market_cap = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return str(self.name)
