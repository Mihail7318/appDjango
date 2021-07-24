from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField


class Fed(models.Model):

    STATUS_NEWS = (
        ('Publish', 'Опубликовать'),
        ('Not_to_publish', 'Не публиковать'),
    )

    status = models.CharField(default='P',max_length=30, choices=STATUS_NEWS, verbose_name='Статус')
    yved = models.BooleanField(default=False, verbose_name='Уведомить')
    title = models.CharField(max_length=255, db_index=True, verbose_name='Наименование')
    slug = models.CharField(max_length=255, db_index=True, verbose_name='Ссылка')
    image = models.ImageField(blank=True, upload_to='media/image/', null=True, verbose_name='Изображение')
    views = models.IntegerField(default=0, verbose_name='Количество просмотров')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    update_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Федеральный'
        verbose_name_plural = 'Федеральный'
        ordering = ['-created_at']


class Reg(models.Model):

    STATUS_NEWS = (
        ('Publish', 'Опубликовать'),
        ('Not_to_publish', 'Не публиковать'),
    )

    status = models.CharField(default='P',max_length=30, choices=STATUS_NEWS, verbose_name='Статус')
    yved = models.BooleanField(default=False, verbose_name='Уведомить')
    title = models.CharField(max_length=255, db_index=True, verbose_name='Наименование')
    slug = models.CharField(max_length=255,verbose_name='Ссылка')
    image = models.ImageField(blank=True, upload_to='media/image/', null=True, verbose_name='Изображение')
    views = models.IntegerField(default=0, verbose_name='Количество просмотров')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    update_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Регеональный'
        verbose_name_plural = 'Региональный'
        ordering = ['-created_at']

