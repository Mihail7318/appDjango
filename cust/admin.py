from django.contrib import admin
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django.utils.safestring import mark_safe
from modeltranslation.admin import TranslationAdmin

# Register your models here.
from cust.models import Standartpages, Partner, Faq, Document, Setting




class StandartpagesAdminForm(forms.ModelForm):
    """Форма с виджетом ckeditor"""
    content_ru = forms.CharField(label="Описание", widget=CKEditorUploadingWidget())
    content_en = forms.CharField(label="Описание", widget=CKEditorUploadingWidget())

    class Meta:
        model = Standartpages
        fields = '__all__'

@admin.register(Standartpages)
class StandartpagesAdmin(TranslationAdmin):
    save_on_top = True
    def has_add_permission(self, request):
        num_objects = self.model.objects.count()
        if num_objects >= 1:
            return False
        else:
            return True

@admin.register(Faq)
class FaqAdmin(TranslationAdmin):
    save_on_top = True


@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    save_on_top = True


@admin.register(Setting)
class SettingAdmin(TranslationAdmin):
    save_on_top = True
    def has_add_permission(self, request):
        num_objects = self.model.objects.count()
        if num_objects >= 1:
            return False
        else:
            return True

@admin.register(Partner)
class PartnerAdmin(admin.ModelAdmin):
    save_as = True
    save_on_top = True
    list_display = ('id', 'name', 'get_image')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    readonly_fields = ('get_image',)

    def get_image(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" width="50">')
        return '-'

    get_image.short_description = 'минеатюра'
