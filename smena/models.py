from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.urls import reverse

from news.models import *

# Create your models here.


class Smena(models.Model):

    STATUS_NEWS = (
        ('Publish', 'Опубликовать'),
        ('Not_to_publish', 'Не публиковать'),
    )

    status = models.CharField(default='P',max_length=30, choices=STATUS_NEWS, verbose_name='Статус')
    yved = models.BooleanField(default=False, verbose_name='Уведомить')
    title = models.CharField(max_length=255, db_index=True, verbose_name='Наименование')
    slug = models.SlugField(unique=True, verbose_name='Ссылка')
    rubric = models.ForeignKey('rubric', on_delete=models.CASCADE, verbose_name='Рубрика')
    content = RichTextUploadingField(blank=True, verbose_name='Описание')
    image = models.ImageField(blank=True, upload_to='media/image/', null=True, verbose_name='Изображение')
    views = models.IntegerField(default=0, verbose_name='Количество просмотров')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    update_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post', kwargs={"slug": self.slug})

    class Meta:
        verbose_name = 'Профильная смена'
        verbose_name_plural = 'Профильные смены'
        ordering = ['-created_at']


class Rubric(models.Model):
    name = models.CharField(max_length=250, verbose_name="Название рубрики")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'рубрики смены'
        verbose_name_plural = 'рубрика смены'



