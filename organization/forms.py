from django import forms
from organization.models import Order


class OrderBaseForm(forms.ModelForm):
    """
    Базовая форма Order
    """

    class Meta:
        model = Order
        fields = '__all__'


class OrderCreateForm(OrderBaseForm):
    """
    Форма Создание Order
    """

    pass


class OrderUpdateForm(OrderBaseForm):
    """
    Форма Редактирование Order
    """

    pass
