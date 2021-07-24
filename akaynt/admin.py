from django.contrib import admin

from .models import *


@admin.register(CustomUseris)
class CustomUserisAdmin(admin.ModelAdmin):
    list_display = ('id',)
    save_as = True
    save_on_top = True



admin.site.register(Customer)
