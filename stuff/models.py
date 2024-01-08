from datetime import timedelta
from django.db import models
from django.utils import timezone
from stuff.choices import GenderChoices


class People(models.Model):
    """
    Человек
    """

    first_name = models.CharField('Имя', max_length=256)
    last_name = models.CharField('Фамилия', max_length=256, blank=True, null=True)
    birth_date = models.DateField('Дата рождения',  default=timezone.now() - timedelta(days=30*365))
    gender = models.IntegerField('Пол', choices=GenderChoices.choices, default=GenderChoices.MALE)

    class Meta:
        verbose_name = 'Человек'
        verbose_name_plural = 'Люди'
        abstract = True

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Trader(People):
    """
    Продавец
    """

    position = models.CharField('Должность', max_length=256, default='Продавец')

    class Meta:
        verbose_name = 'Продавец'
        verbose_name_plural = 'Продавцы'
        ordering = ('-first_name',)

    def __str__(self):
        return f'{self.position} {self.first_name}'


class Leader(People):
    """
    Руководитель
    """

    position = models.CharField('Должность', max_length=256, default='Руководитель')

    class Meta:
        verbose_name = 'Руководитель'
        verbose_name_plural = 'Руководители'
        ordering = ('-first_name',)

    def __str__(self):
        return f'{self.position} {self.first_name}'
