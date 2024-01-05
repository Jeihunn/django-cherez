from modeltranslation.translator import translator, TranslationOptions
from .models import ProductCategory, ProductAdditional, Product


class ProductCategoryTranslationOptions(TranslationOptions):
    fields = ("title",)


class ProductAdditionalTranslationOptions(TranslationOptions):
    fields = ("title",)


class ProductTranslationOptions(TranslationOptions):
    fields = ("title", "short_description", "description")


translator.register(ProductCategory, ProductCategoryTranslationOptions)
translator.register(ProductAdditional, ProductAdditionalTranslationOptions)
translator.register(Product, ProductTranslationOptions)