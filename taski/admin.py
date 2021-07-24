from django.contrib import admin
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django.utils.safestring import mark_safe
from mptt.admin import DraggableMPTTAdmin
from modeltranslation.admin import TranslationAdmin

from .models import *

class ZadachaAdminForm(forms.ModelForm):
    """Форма с виджетом ckeditor"""
    content_ru = forms.CharField(label="Описание", widget=CKEditorUploadingWidget())
    content_en = forms.CharField(label="Описание", widget=CKEditorUploadingWidget())

    class Meta:
        model = Post
        fields = '__all__'




'''
@admin.register(Vopros)
class VoprosAdmin(TranslationAdmin):
    list_display = ('id', 'title', 'created_at', 'views', )
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content', 'views')
    form = ZadachaAdminForm
    save_as = True
    save_on_top = True'''

class VoprosInline(admin.TabularInline):
    fk_name = 'zadacha'
    model = Vopros
    extra = 1

@admin.register(Zadacha)
class ZadachaAdmin(TranslationAdmin):
    inlines = [VoprosInline]
    list_display = ('id', 'title', 'rubric', 'created_at', 'status', 'views', )
    prepopulated_fields = {'slug': ('title',)}
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content', 'views')
    list_editable = ('status',)
    list_filter = ('status', 'rubric',)
    form = ZadachaAdminForm
    save_as = True
    save_on_top = True


