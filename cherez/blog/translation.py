from modeltranslation.translator import translator, TranslationOptions
from .models import BlogCategory, BlogPost


class BlogCategoryTranslationOptions(TranslationOptions):
    fields = ("title",)


class BlogPostTranslationOptions(TranslationOptions):
    fields = ("title", "short_description", "content")


translator.register(BlogCategory, BlogCategoryTranslationOptions)
translator.register(BlogPost, BlogPostTranslationOptions)
