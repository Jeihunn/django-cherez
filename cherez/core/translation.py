from modeltranslation.translator import translator, TranslationOptions
from .models import FAQ, HomeAdvantage


class FAQTranslationOptions(TranslationOptions):
    fields = ("question", "answer")


class HomeAdvantageTranslationOptions(TranslationOptions):
    fields = ("title", "description")


translator.register(HomeAdvantage, HomeAdvantageTranslationOptions)
translator.register(FAQ, FAQTranslationOptions)