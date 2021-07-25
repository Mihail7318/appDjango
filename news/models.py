from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.urls import reverse
from mptt.models import MPTTModel, TreeForeignKey
from django.conf import settings
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericRelation


class Category(MPTTModel):

    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children', verbose_name='Родитель')
    name = models.CharField(max_length=255, verbose_name='Имя рубрики')
    slug = models.SlugField(max_length=255, unique=True, verbose_name='Ссылка')
    photo = models.ImageField(blank=True, upload_to='image', null=True, verbose_name='Изображение')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={"slug": self.slug})

    class MPTTMeta:
        order_insertion_by = ['name']

    class Meta:
        verbose_name = 'Рубрика'
        verbose_name_plural = 'Рубрики'


class Tag(models.Model):

    BUTTON = (
        ('Publish', 'Опубликовать'),
        ('Not_to_publish', 'Не публиковать'),
    )

    button = models.CharField(max_length=30, choices=BUTTON, verbose_name='Статус')
    name = models.CharField(max_length=30, verbose_name='Название(ru)')
    image = models.ImageField(blank=True,  null=True, verbose_name='Изображение')
    slug = models.SlugField(max_length=255, unique=True, verbose_name='Ссылка')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('tag', kwargs={"slug": self.slug})

    class Meta:
        verbose_name = 'Метка'
        verbose_name_plural = 'Метки'
        ordering = ['name']





class Post(models.Model):

    author = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='Автор', on_delete=models.CASCADE)

    STATUS_NEWS = (
        ('Publish', 'Опубликовать'),
        ('Not_to_publish', 'Не публиковать'),
    )

    status = models.CharField(default='P',max_length=30, choices=STATUS_NEWS, verbose_name='Статус')
    yved = models.BooleanField(default=False, verbose_name='Уведомить')
    title = models.CharField(max_length=255, db_index=True, verbose_name='Наименование')
    slug = models.SlugField(unique=True, verbose_name='Ссылка')
    content = RichTextUploadingField(blank=True, verbose_name='Описание')
    category = TreeForeignKey('Category', verbose_name='Рубрики', on_delete=models.CASCADE, null=True, blank=True, db_index=True)
    tags = models.ManyToManyField(Tag, verbose_name='Тэг')
    image = models.ImageField(blank=True, upload_to='media/image/', null=True, verbose_name='Изображение')
    views = models.IntegerField(default=0, verbose_name='Количество просмотров')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    update_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post', kwargs={"slug": self.slug})

    class Meta:
        verbose_name = 'Статья(ю)'
        verbose_name_plural = 'Статьи'
        ordering = ['-created_at']

class Comment(models.Model):

    user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='автор', on_delete=models.CASCADE)
    text = models.TextField(verbose_name='текст коментария')
    parent = models.ForeignKey('self', verbose_name='Коментарий к коментарию', blank=True, null=True, related_name='comment_children', on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now=True, verbose_name='Дата создания комментария')
    is_child = models.BooleanField(default=False)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name='Пост')
    def __str__(self):
        return str(self.id)

    @property
    def get_parent(self):
        if not self.parent:
            return ""
        return self.parent

class Complain(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='автор', on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name='Запись')
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, verbose_name='Коментарий')
