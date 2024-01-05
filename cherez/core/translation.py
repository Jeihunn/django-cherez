from modeltranslation.translator import translator, TranslationOptions
from .models import FAQ


class FAQTranslationOptions(TranslationOptions):
    fields = ("question", "answer")


translator.register(FAQ, FAQTranslationOptions)