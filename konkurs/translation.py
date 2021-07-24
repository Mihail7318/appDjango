from modeltranslation.translator import register, TranslationOptions
from .models import *

@register(Fed)
class FedTranslationOptions(TranslationOptions):
    fields = ('title',)

@register(Reg)
class RedTranslationOptions(TranslationOptions):
    fields = ('title',)
