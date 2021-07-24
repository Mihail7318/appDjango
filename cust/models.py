from __future__ import unicode_literals

from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models


class Setting(models.Model):

    title = models.CharField(max_length=30, verbose_name='Название')
    keyword = models.CharField(max_length=255, verbose_name='Ключевые слова')
    description = models.CharField(max_length=255, verbose_name='Описание')
    copyright = models.CharField(max_length=255, verbose_name='copyright')
    favicon = models.ImageField(blank=True, upload_to='images/', verbose_name='Иконка сайта')
    logotip = models.ImageField(blank=True, upload_to='images/', verbose_name='Логотип')
    address = models.CharField(blank=True, max_length=100, verbose_name='Адрес')
    phone = models.CharField(blank=True, max_length=15, verbose_name='Телефон')
    email = models.CharField(blank=True, max_length=50, verbose_name='Электроная почта')
    smtpserver = models.CharField(blank=True, max_length=50, verbose_name='SMTPserver')
    smtpemail = models.CharField(blank=True, max_length=50, verbose_name='SMTPemail')
    smtppassword = models.CharField(blank=True, max_length=50, verbose_name='SMTPpassword')
    smtpport = models.CharField(blank=True, max_length=8, verbose_name='SMTPport')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Общие настроики"
        verbose_name_plural = "Общие настроики"

class Standartpages(models.Model):

    privacypolicy = RichTextUploadingField(blank=True, verbose_name='Политика конфиденциальности')
    useragreement = RichTextUploadingField(blank=True, verbose_name='Пользовательское соглашение')
    contact = RichTextUploadingField(blank=True, verbose_name='Контакты')
    aboutus = RichTextUploadingField(blank=True, verbose_name='О нас')

    class Meta:
        verbose_name = "стандартные страницы"
        verbose_name_plural = "стандартные страницы"

class Faq(models.Model):

    problem = models.TextField (max_length=255, verbose_name='Вопрос')
    reply = models.TextField(verbose_name='Ответ')

    def __str__(self):
        return self.problem

    class Meta:
        verbose_name = "ЧаВо"
        verbose_name_plural = "ЧаВо"

class Partner(models.Model):

    BUTTON = (
        ('Publish', 'Опубликовать'),
        ('Not_to_publish', 'Не публиковать'),
    )

    button = models.CharField(max_length=30, choices=BUTTON, verbose_name='Статус')
    name = models.CharField(max_length=30, verbose_name='Название')
    ssilka = models.CharField(max_length=30, verbose_name='Ссылка')
    image = models.ImageField(blank=True,  null=True, verbose_name='Изображение')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Партнер'
        verbose_name_plural = 'Партнеры'
        ordering = ['name']

class Document(models.Model):
    file_obj = models.FileField(upload_to='media/')
    name = models.CharField(max_length=30, verbose_name='Название')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Документ'
        verbose_name_plural = 'Документы'
        ordering = ['name']