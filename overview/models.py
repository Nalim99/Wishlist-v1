from django.db import models


class Item(models.Model):
    product = models.CharField(max_length=50)
    price = models.n
