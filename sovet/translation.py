from modeltranslation.translator import register, TranslationOptions
from .models import *

@register(Popsov)
class PopsovTranslationOptions(TranslationOptions):
    fields = ('title', 'doljnost',"works",  )

@register(Exsov)
class ExsovTranslationOptions(TranslationOptions):
    fields = ('title', 'doljnost',"works",  )
