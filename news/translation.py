from modeltranslation.translator import register, TranslationOptions
from .models import *


@register(Category)
class RedTranslationOptions(TranslationOptions):
    fields = ('name',)


@register(Tag)
class RedTranslationOptions(TranslationOptions):
    fields = ('name',)

@register(Post)
class FedTranslationOptions(TranslationOptions):
    fields = ('title','content',)



