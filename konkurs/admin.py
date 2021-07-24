from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

from .models import *
from django import forms


class FedAdminForm(forms.ModelForm):
    """Форма с виджетом ckeditor"""
    title_ru = forms.CharField(label="Описание", widget=CKEditorUploadingWidget())
    title_en = forms.CharField(label="Описание", widget=CKEditorUploadingWidget())

    class Meta:
        model = Fed
        fields = '__all__'


class RegAdminForm(forms.ModelForm):
    """Форма с виджетом ckeditor"""
    title_ru = forms.CharField(label="Описание", widget=CKEditorUploadingWidget())
    title_en = forms.CharField(label="Описание", widget=CKEditorUploadingWidget())

    class Meta:
        model = Reg
        fields = '__all__'


@admin.register(Fed)
class FedAdmin(TranslationAdmin):
    list_display = ('id', 'title', 'created_at', 'status', 'views', )
    prepopulated_fields = {'slug': ('title',)}
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content', 'views')
    list_editable = ('status',)
    list_filter = ('status',)
    #form = FedAdminForm
    save_as = True
    save_on_top = True


@admin.register(Reg)
class RegAdmin(TranslationAdmin):
    list_display = ('id', 'title', 'created_at', 'status', 'views', )
    prepopulated_fields = {'slug': ('title',)}
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content', 'views')
    list_editable = ('status',)
    list_filter = ('status',)
    #form = RegAdminForm
    save_as = True
    save_on_top = True

