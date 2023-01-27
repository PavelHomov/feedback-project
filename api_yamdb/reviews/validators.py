from django.core.exceptions import ValidationError
from django.utils import timezone


def validator_year(value):
    if value > timezone.now().year:
        raise ValidationError(
            f'Год {value} больше текущего'
        )
