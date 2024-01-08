from django.views.generic import CreateView, UpdateView, ListView, DetailView
from organization.forms import OrderCreateForm, OrderUpdateForm
from organization.models import Organization, Order, TradePoint, Supplier


class OrderListView(ListView):
    """
    Список Заказов
    """

    model = Order
    template_name = 'organization/order/list.html'


class OrderCreateView(CreateView):
    """
    Создание Заказа
    """

    model = Order
    template_name = 'organization/order/create.html'
    form_class = OrderCreateForm

    def get_success_url(self):
        return self.object.get_detail_url()


class OrderUpdateView(UpdateView):
    """
    Редактирование Заказа
    """

    model = Order
    template_name = 'organization/order/update.html'
    form_class = OrderUpdateForm

    def get_success_url(self):
        return self.object.get_detail_url()


class OrderDetailView(DetailView):
    """
    Просмотр Заказа
    """

    model = Order
    template_name = 'organization/order/detail.html'


class TradePointListView(ListView):
    """
    Список Торговых точек
    """

    model = TradePoint
    template_name = 'organization/trade_point/list.html'


class TradePointDetailView(DetailView):
    """
    Просмотр Торговой точки
    """

    model = TradePoint
    template_name = 'organization/trade_point/detail.html'


class SupplierListView(ListView):
    """
    Список поставщиков
    """

    model = Supplier
    template_name = 'organization/supplier/list.html'


class SupplierDetailView(DetailView):
    """
    Просмотр поставщика
    """

    model = Supplier
    template_name = 'organization/supplier/detail.html'


class OrganizationListView(ListView):
    """
    Список организаций
    """

    model = Organization
    template_name = 'organization/list.html'


class OrganizationDetailView(DetailView):
    """
    Просмотр Организации
    """

    model = Organization
    template_name = 'organization/detail.html'
