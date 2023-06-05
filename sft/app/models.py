from django.db import models


class Contract(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Bid(models.Model):
    title = models.CharField(max_length=100)
    contract = models.ForeignKey(Contract, on_delete=models.CASCADE, related_name='bids')

    def __str__(self):
        return self.title


class Manufacturer(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Product(models.Model):
    title = models.CharField(max_length=100)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE, related_name='products')
    bid = models.ForeignKey(Bid, null=True, blank=True, on_delete=models.CASCADE, related_name='products')

    def __str__(self):
        return f"{self.title} | manufacturer: {self.manufacturer}"
