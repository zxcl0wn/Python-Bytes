from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator, MaxLengthValidator
from django.db import models
from django.utils import timezone


class Post(models.Model):
    title = models.CharField(max_length=100, verbose_name='Заголовок', null=False, validators=[
                                MinLengthValidator(5, message="Минимум 5 символов"),
                                MaxLengthValidator(100, message="Максимум 100 символов"),
                            ])
    content = models.TextField(max_length=1500, verbose_name='Содержание', null=False, validators=[
                                MinLengthValidator(50, message="Минимум 50 символов"),
                                MaxLengthValidator(1500, message="Максимум 1500 символов"),
                            ])
    date_posted = models.DateTimeField(default=timezone.now, verbose_name='Дата публикации')
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, verbose_name='Автор')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Публикация'
        verbose_name_plural = 'Публикации'
