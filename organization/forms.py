from django import forms
from organization.models import Order


class OrderBaseForm(forms.ModelForm):
    """
    Базовая форма Order
    """

    class Meta:
        model = Order
        fields = '__all__'
        widgets = {
            'trade_point': forms.Select(attrs={'class': 'form-control'}),
            'supplier': forms.Select(attrs={'class': 'form-control'}),
            'product_name': forms.TextInput(attrs={'class': 'form-control'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
        }


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
