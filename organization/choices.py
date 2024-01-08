from django.db.models import IntegerChoices


class TradePointType(IntegerChoices):
    """
    Роли Сотрудников
    """

    SMALL = 1, 'Киоск'
    MEDIUM = 5, 'Магазин'
    BIG = 10, 'Универмаг'
