from django.db import models


class Course(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название товара:')
    instructor = models.CharField(max_length=255, verbose_name='Страна производитель:')
    price_per_month = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена:')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
