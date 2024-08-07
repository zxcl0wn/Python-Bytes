from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    image = models.ImageField(default='default.jpg', upload_to='profile_pics', verbose_name='Изображение')

    def __str__(self):
        return f'{self.user.username} Profile'

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'
