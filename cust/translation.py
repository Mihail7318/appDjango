from modeltranslation.translator import register, TranslationOptions
from .models import Faq, Standartpages, Setting

@register(Faq)
class FaqTranslationOptions(TranslationOptions):
    fields = ('problem', 'reply')

@register(Standartpages)
class StandartpagesTranslationOptions(TranslationOptions):
    fields = ('privacypolicy', 'useragreement', 'contact', 'aboutus')


@register(Setting)
class SettingTranslationOptions(TranslationOptions):
    fields = ('title', 'keyword', 'description', 'copyright', 'address')
