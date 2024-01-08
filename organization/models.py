from django.db import models
from django.urls import reverse_lazy

from organization.choices import TradePointType


class Organization(models.Model):
    """
    Торговая организация
    """

    name = models.CharField('Название', max_length=5000)
    address = models.CharField('Адрес', max_length=5000, blank=True, null=True)
    inn = models.CharField('ИНН', max_length=100, blank=True, null=True)
    leader = models.ForeignKey(
        'stuff.Leader', verbose_name='Руководитель', related_name='organizations', blank=True, null=True, on_delete=models.SET_NULL
    )

    class Meta:
        verbose_name = 'Торговая организация'
        verbose_name_plural = 'Торговые организации'
        ordering = ('-name',)

    def __str__(self):
        return self.name


class TradePoint(models.Model):
    """
    Торговая точка
    """

    name = models.CharField('Название', max_length=5000)
    type = models.IntegerField(
        'Тип торговой точки', choices=TradePointType.choices, default=TradePointType.MEDIUM
    )
    organization = models.ForeignKey(
        Organization, verbose_name='Торговая организация', related_name='trade_points', on_delete=models.CASCADE
    )
    address = models.CharField('Адрес', max_length=5000, blank=True, null=True)
    leader = models.ForeignKey(
        'stuff.Leader', verbose_name='Руководитель', related_name='trade_points', on_delete=models.SET_NULL, null=True, blank=True
    )

    class Meta:
        verbose_name = 'Торговая точка'
        verbose_name_plural = 'Торговые точки'
        ordering = ('-name',)

    def __str__(self):
        return f'{self.get_type_display()} {self.name}'


class Supplier(models.Model):
    """
    Поставщик
    """

    name = models.CharField('Название', max_length=5000)
    country = models.CharField('Название страны', max_length=5000, default='Россия', blank=True)

    class Meta:
        verbose_name = 'Поставщик'
        verbose_name_plural = 'Поставщики'
        ordering = ('-country', '-name',)

    def __str__(self):
        return self.name


class Order(models.Model):
    """
    Заказ поставщикам
    """

    date = models.DateTimeField('Дата заказа', auto_now_add=True)
    trade_point = models.ForeignKey(TradePoint, verbose_name='Торговая точка', related_name='orders', on_delete=models.CASCADE)
    supplier = models.ForeignKey(Supplier, verbose_name='Поставщик', related_name='orders', on_delete=models.CASCADE)
    product_name = models.CharField('Название товара', max_length=5000)
    quantity = models.PositiveIntegerField('Количество товара', default=1, blank=True)
    price = models.DecimalField('Цена', max_digits=10, decimal_places=2)

    class Meta:
        verbose_name = 'Заказ поставщикам'
        verbose_name_plural = 'Заказы поставщикам'
        ordering = ('-product_name',)

    def __str__(self):
        return self.product_name

    def get_detail_url(self):
        return reverse_lazy('organization:order-detail', kwargs={'pk': self.pk})
