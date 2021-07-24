from news.models import *
from django.contrib.auth.models import User

from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField



class Zadacha(models.Model):

    STATUS_NEWS = (
        ('Publish', 'Опубликовать'),
        ('Not_to_publish', 'Не публиковать'),
    )

    status = models.CharField(default='Publish', max_length=30, choices=STATUS_NEWS, verbose_name='Статус')
    yved = models.BooleanField(default=False, verbose_name='Уведомить')
    title = models.CharField(max_length=255, db_index=True, verbose_name='Наименование')
    slug = models.SlugField(unique=True, verbose_name='Ссылка')
    content = RichTextUploadingField(blank=True, verbose_name='Описание')
    rubric = models.ForeignKey('news.Category', on_delete=models.CASCADE, verbose_name='Рубрика')
    image = models.ImageField(blank=True, upload_to='media/image/', null=True, verbose_name='Изображение')
    views = models.IntegerField(default=0, verbose_name='Количество просмотров')
    time = models.TimeField(default=0, verbose_name='Время просмотров')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    update_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post', kwargs={"slug": self.slug})

    class Meta:
        verbose_name = 'Задание(ю)'
        verbose_name_plural = 'Задания'
        ordering = ['-created_at']




class Vopros(models.Model):

    zadacha = models.ForeignKey(Zadacha, on_delete=models.CASCADE, related_name='voprosiki')
    author = models.ForeignKey(User, default='self', related_name='poster', on_delete=models.CASCADE)
    title = models.CharField(max_length=255, db_index=True, verbose_name='Наименование')
    content = RichTextUploadingField(blank=True, verbose_name='Описание')
    image = models.ImageField(blank=True, upload_to='media/image/', null=True, verbose_name='Изображение задачи')
    image_1 = models.ImageField(blank=True, upload_to='media/image/', null=True, verbose_name='Изображение')
    varian_1 = models.CharField(max_length=255, db_index=True, verbose_name='Ответ №1')
    otvet_1 = models.BooleanField(default=False, verbose_name='Верный')
    image_2 = models.ImageField(blank=True, upload_to='media/image/', null=True, verbose_name='Изображение')
    varian_2 = models.CharField(max_length=255, db_index=True, verbose_name='Ответ №2')
    otvet_2 = models.BooleanField(default=False, verbose_name='Верный')
    image_3 = models.ImageField(blank=True, upload_to='media/image/', null=True, verbose_name='Изображение')
    varian_3 = models.CharField(max_length=255, db_index=True, verbose_name='Ответ №3')
    otvet_3 = models.BooleanField(default=False, verbose_name='Верный')
    image_4 = models.ImageField(blank=True, upload_to='media/image/', null=True, verbose_name='Изображение')
    varian_4 = models.CharField(max_length=255, db_index=True, verbose_name='Ответ №4')
    otvet_4 = models.BooleanField(default=False, verbose_name='Верный')
    views = models.IntegerField(default=0, verbose_name='Количество пройденых')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    update_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Тест'
        verbose_name_plural = 'Тесты'
        ordering = ['-created_at']


