from django.db import models


class Item(models.Model):
    product = models.CharField(max_length=50)
    price = models.IntegerField(default=0)
    category = models.IntegerField(default=0)
    priority = models.IntegerField(default=0)  # priority level from Low, Medium to High (value 0-2)
    hyperlink = models.CharField(max_length=1024)
    archived = models.BooleanField(default=False)
    description = models.CharField(max_length=1024)

    def __str__(self):
        return '[' + str(self.id) + '] ' + self.product + ' for: ' + str(self.price)
