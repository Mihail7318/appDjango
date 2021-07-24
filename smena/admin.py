from django.contrib import admin
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django.utils.safestring import mark_safe
from modeltranslation.admin import TranslationAdmin
from .models import *

class SmenaAdminForm(forms.ModelForm):
    """Форма с виджетом ckeditor"""
    content_ru = forms.CharField(label="Описание[ru]", widget=CKEditorUploadingWidget())
    content_en = forms.CharField(label="Описание[en]", widget=CKEditorUploadingWidget())

    class Meta:
        model = Smena
        fields = '__all__'

@admin.register(Smena)
class SmenaAdmin(TranslationAdmin):
    list_display = ('id', 'title', 'rubric', 'created_at', 'status', 'views', )
    prepopulated_fields = {'slug': ('title',)}
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content', 'views')
    list_editable = ('status',)
    list_filter = ('status', 'rubric',)
    form = SmenaAdminForm
    save_as = True
    save_on_top = True

@admin.register(Rubric)
class RubricAdmin(TranslationAdmin):
    fields = ('name',)

