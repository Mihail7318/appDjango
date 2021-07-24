from modeltranslation.translator import register, TranslationOptions
from .models import Zadacha, Vopros

@register(Zadacha)
class ZadachaTranslationOptions(TranslationOptions):
    fields = ('title', 'content')

@register(Vopros)
class VoprosTranslationOptions(TranslationOptions):
    fields = ('title', 'content')
