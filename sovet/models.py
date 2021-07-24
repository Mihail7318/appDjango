from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from django.urls import reverse

class Popsov(models.Model):

    STATUS_NEWS = (
        ('Publish', 'Опубликовать'),
        ('Not_to_publish', 'Не публиковать'),
    )

    status = models.CharField(default='P',max_length=30, choices=STATUS_NEWS, verbose_name='Статус')
    title = models.CharField(max_length=255, db_index=True, verbose_name='Имя')
    doljnost = models.CharField(max_length=255, db_index=True, verbose_name='Должность')
    works = models.CharField(max_length=255, db_index=True, verbose_name='Место работы')
    image = models.ImageField(blank=True, upload_to='media/image/', null=True, verbose_name='Фото')
    views = models.IntegerField(default=0, verbose_name='Количество просмотров')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    update_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Попечительский совет'
        verbose_name_plural = 'Попечительский совет'
        ordering = ['-created_at']


class Exsov(models.Model):

    STATUS_NEWS = (
        ('Publish', 'Опубликовать'),
        ('Not_to_publish', 'Не публиковать'),
    )

    status = models.CharField(default='Publish', max_length=30, choices=STATUS_NEWS, verbose_name='Статус')
    title = models.CharField(max_length=255, db_index=True, verbose_name='Имя')
    doljnost = models.CharField(max_length=255, db_index=True, verbose_name='Должность')
    works = models.CharField(max_length=255, db_index=True, verbose_name='Место работы')
    image = models.ImageField(blank=True, upload_to='media/image/', null=True, verbose_name='Фото')
    views = models.IntegerField(default=0, verbose_name='Количество просмотров')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    update_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Экспертный совет'
        verbose_name_plural = 'Экспертный совет'
        ordering = ['-created_at']


