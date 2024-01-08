from django.contrib import admin
from organization.models import Organization, TradePoint, Order, Supplier


@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    """
    Админка: Organization
    """

    pass


@admin.register(TradePoint)
class TradePointAdmin(admin.ModelAdmin):
    """
    Админка: TradePoint
    """

    pass


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    """
    Админка: Order
    """

    pass


@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    """
    Админка: Supplier
    """

    pass
