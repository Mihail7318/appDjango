from django.contrib import admin
from ckeditor_uploader.widgets import CKEditorUploadingWidget

from modeltranslation.admin import TranslationAdmin
from django import forms

from .models import *

class PostAdminForm(forms.ModelForm):
    """Форма с виджетом ckeditor"""
    content_ru = forms.CharField(label="Описание", widget=CKEditorUploadingWidget())
    content_en = forms.CharField(label="Описание", widget=CKEditorUploadingWidget())

    class Meta:
        model = Post
        fields = '__all__'

@admin.register(Post)
class PostAdmin(TranslationAdmin):
    list_display = ('id', 'title', 'category', 'created_at', 'status', 'views', )
    prepopulated_fields = {'slug': ('title',)}
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content', 'views')
    list_editable = ('status',)
    list_filter = ('status', 'category', 'tags',)
    form = PostAdminForm
    save_as = True
    save_on_top = True