from django.db import models

# Create your models here.
class Item(models.Model):
    product = models.CharField(max_length=30)
    value = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    qty = models.PositiveIntegerField(null=False,)

    def __str__(self):
        return self.product