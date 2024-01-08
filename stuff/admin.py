from django.contrib import admin
from stuff.models import Leader, Trader


@admin.register(Leader)
class LeaderAdmin(admin.ModelAdmin):
    """
    Админка: Leader
    """

    pass


@admin.register(Trader)
class TraderAdmin(admin.ModelAdmin):
    """
    Админка: Trader
    """

    pass
