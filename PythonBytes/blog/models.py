from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class Post(models.Model):
    title = models.CharField(max_length=100, verbose_name='Заголовок', null=False)
    content = models.TextField(max_length=500, verbose_name='Содержание', null=False)
    date_posted = models.DateTimeField(default=timezone.now, verbose_name='Дата публикации')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Публикация'
        verbose_name_plural = 'Публикации'
