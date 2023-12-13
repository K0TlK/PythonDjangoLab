from django.db import models


class Supply(models.Model):
    name = models.CharField(max_length=200)  # Название поставки
    quantity = models.IntegerField()  # Количество товара
    delivery_date = models.DateField()  # Дата поставки

    def __str__(self):
        return self.name
