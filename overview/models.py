from django.db import models


class Item(models.Model):
    product = models.CharField(max_length=50)
    price = models.IntegerField(default=0)
    category = models.ForeignKey('Category', default=None, null=True, blank=True, on_delete=models.CASCADE,)
    priority = models.IntegerField(default=0)  # priority level from Low, Medium to High (value 0-2)
    hyperlink = models.CharField(max_length=1024, null=True, blank=True)
    archived = models.BooleanField(default=False)
    description = models.CharField(max_length=1024, null=True, blank=True)

    def __str__(self):
        return '[' + str(self.id) + '] ' + self.product + ' : €' + str(self.price)

class Category(models.Model):
    name = models.CharField(max_length=50)
    color = models.CharField(max_length=6)  # hexcode as color

    def __str__(self):
        return '[' + str(self.id) + '] ' + self.name
