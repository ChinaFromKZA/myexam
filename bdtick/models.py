from django.db import models


class Products(models.Model):
    title = models.CharField('Название', max_length=30)
    names = models.CharField('Цена', max_length=60)
    full_text = models.TextField('Информация')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'

