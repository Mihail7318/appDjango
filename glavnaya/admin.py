from django.contrib import admin
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django.utils.safestring import mark_safe
from news.models import *
from mptt.admin import DraggableMPTTAdmin

# Register your models here.
from .models import *

@admin.register(Slider)
class SliderAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_at', )
    list_display_links = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'views')

    save_as = True
    save_on_top = True

@admin.register(Vidjet)
class VidjetAdmin(admin.ModelAdmin):
    save_on_top = True
    def has_add_permission(self, request):
        num_objects = self.model.objects.count()
        if num_objects >= 1:
            return False
        else:
            return True


@admin.register(Favorit)
class FavoritAdmin(admin.ModelAdmin):
    save_on_top = True
    def has_add_permission(self, request):
        num_objects = self.model.objects.count()
        if num_objects >= 1:
            return False
        else:
            return True


@admin.register(Favorites)
class FavoritesAdmin(admin.ModelAdmin):
    save_on_top = True
    def has_add_permission(self, request):
        num_objects = self.model.objects.count()
        if num_objects >= 1:
            return False
        else:
            return True



@admin.register(Saidebar)
class SaidebarAdmin(admin.ModelAdmin):
    save_on_top = True
    def has_add_permission(self, request):
        num_objects = self.model.objects.count()
        if num_objects >= 1:
            return False
        else:
            return True


@admin.register(Footer)
class FooterAdmin(admin.ModelAdmin):
    save_on_top = True



@admin.register(Menu)
class MenuAdmin(DraggableMPTTAdmin):
    save_on_top = True


class IkonkiAdmin(admin.ModelAdmin):
    list_display = ['title', 'icon']

admin.site.register(Ikonki,IkonkiAdmin)

