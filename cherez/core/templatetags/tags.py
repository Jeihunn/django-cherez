from django import template

from product.models import ProductCategory

register = template.Library()


@register.filter
def remove_param(value: dict, param: str) -> str:
    """
    Custom template filter to remove a parameter from the query string.
    Usage: {{ request.GET|remove_param:"param_to_remove" }}
    """
    params = value.copy()

    if param in params:
        del params[param]

    return params.urlencode()


@register.simple_tag
def get_parent_null_categories():
    """
    Custom template tag to retrieve categories with a None parent.
    Usage: {% get_parent_null_categories as parent_null_categories %}
    """
    parent_null_categories = ProductCategory.objects.filter(parent=None)
    return parent_null_categories