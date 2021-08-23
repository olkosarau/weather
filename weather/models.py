from django.db import models


class City(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название города')
    temp = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='Температура', blank=True, default='1')

    def __str__(self):
        return self.name

