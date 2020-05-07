import os
from django.core.exceptions import ValidationError


def validate_csv(value):
    ext = os.path.splitext(value.name)[1]
    if os.path.splitext(value.name)[1].lower() != '.csv':
        raise ValidationError('Необходимо загрузить файл с расширением ".csv"')