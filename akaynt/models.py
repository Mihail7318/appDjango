from django.db import models
from django.urls import reverse

from django.contrib.auth.models import User

from news.models import *

from django.contrib.auth import get_user_model
from django.contrib.contenttypes.models import ContentType
from django.utils import timezone

User = get_user_model()


class Customer(models.Model):

    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)
    phone = models.CharField(max_length=20, verbose_name='Номер телефона', null=True, blank=True)
    onli = models.BooleanField(default=False, verbose_name='Ученик онлайн')
    avatar = models.ImageField(upload_to='images/users', verbose_name='Изображение', null=True, blank=True, )
    dt = models.DateField(max_length=255, verbose_name='Дата рождения')
    status = models.BooleanField(default=False, verbose_name='Статус')

    def __str__(self):
        return "Пользователь: {} {}".format(self.user.first_name, self.user.last_name)

    class Meta:
        verbose_name = 'Ученик'
        verbose_name_plural = 'Ученики'



class CustomUseris(User):

    class Meta:
        verbose_name = 'Учитель'
        verbose_name_plural = 'Учителя'
