from django.db import models


class Supply(models.Model):
    name = models.CharField(max_length=200)
    quantity = models.IntegerField()
    delivery_date = models.DateField()

    def __str__(self):
        return self.name
