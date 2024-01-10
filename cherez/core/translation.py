from modeltranslation.translator import translator, TranslationOptions
from .models import FAQ, HomeAdvantage, HomeBanner, HomeSlider, AboutUs


class FAQTranslationOptions(TranslationOptions):
    fields = ("question", "answer")


class HomeAdvantageTranslationOptions(TranslationOptions):
    fields = ("title", "description")


class HomeBannerTranslationOptions(TranslationOptions):
    fields = ("title", "description")


class HomeSliderTranslationOptions(TranslationOptions):
    fields = ("title", "description", "button_text")


class AboutUsTranslationOptions(TranslationOptions):
    fields = ("title", "description")


translator.register(FAQ, FAQTranslationOptions)
translator.register(HomeAdvantage, HomeAdvantageTranslationOptions)
translator.register(HomeBanner, HomeBannerTranslationOptions)
translator.register(HomeSlider, HomeSliderTranslationOptions)
translator.register(AboutUs, AboutUsTranslationOptions)
