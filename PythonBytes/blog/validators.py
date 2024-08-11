import re

from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible


@deconstructible
class TitleValid:
    def __init__(self, min_letters=5):
        self.min_letters = min_letters

    def __call__(self, value):
        letters = re.findall(r'[a-zA-Zа-яА-Я]', value)
        print(len(letters))
        if len(letters) < self.min_letters:
            raise ValidationError(
                f"Заголовок должен содержать хотя бы {self.min_letters} букв."
            )
