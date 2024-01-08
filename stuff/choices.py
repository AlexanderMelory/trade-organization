from django.db.models import IntegerChoices


class GenderChoices(IntegerChoices):
    """
    Пол
    """

    MALE = 1, 'Мужчина'
    FEMALE = 2, 'Женщина'