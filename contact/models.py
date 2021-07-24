from __future__ import unicode_literals

from django.db import models



class Contact(models.Model):

    STATUS_NEWS = (
        ('Telephone', ' Телефон'),
        ('Email', 'Почта'),
    )

    status = models.CharField(default='Telephone', max_length=30, choices=STATUS_NEWS, verbose_name='Способ связи')
    email = models.EmailField()
    name = models.CharField(max_length=255, db_index=True, verbose_name='Имя')
    firstname = models.CharField(max_length=255, db_index=True, verbose_name='Фамилия')
    phone = models.CharField(max_length=255, verbose_name='Телефон')
    text = models.TextField(max_length=255, verbose_name='Текст')
    soglasen = models.BooleanField(default=False, verbose_name='Согласен на обработку персональный данных')
    image = models.ImageField(blank=True,  null=True, verbose_name='Изображение')
    date = models.DateTimeField(auto_now_add=True, verbose_name='Дата')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'

