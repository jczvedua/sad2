from django.db import models
import datetime

class Item(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=100, decimal_places=2)
    date_purchased = models.DateField(default=datetime.date.today)
