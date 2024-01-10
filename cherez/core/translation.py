from modeltranslation.translator import translator, TranslationOptions
from .models import FAQ, HomeAdvantage, HomeBanner


class FAQTranslationOptions(TranslationOptions):
    fields = ("question", "answer")


class HomeAdvantageTranslationOptions(TranslationOptions):
    fields = ("title", "description")


class HomeBannerTranslationOptions(TranslationOptions):
    fields = ("title", "description")


translator.register(FAQ, FAQTranslationOptions)
translator.register(HomeAdvantage, HomeAdvantageTranslationOptions)
translator.register(HomeBanner, HomeBannerTranslationOptions)