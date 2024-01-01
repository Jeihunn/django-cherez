from django import template

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
