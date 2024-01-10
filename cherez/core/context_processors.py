from .models import (
    TitleDescription,
)


def title_description_global(request):
    title_description_list = TitleDescription.objects.all()
    return {
        "title_description_list": title_description_list,
    }
