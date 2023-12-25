from django.utils.text import slugify


def create_unique_slug(
        instance: object,
        field_name: str,
        max_length: int = None,
        use_symbol_mapping: bool = False,
        empty_error_msg: str = "Generated unique slug is empty.",
        long_error_msg: str = "Generated unique slug is too long."
) -> str:
    """
    Creates a unique slug for the given model instance.
    Args:
        instance (django.db.models.Model): Model instance for which the slug is to be created.
        field_name (str): Field name to be used for creating the slug.
        max_length (int, optional): Maximum length for the slug. Defaults to None.
        use_symbol_mapping (bool, optional): Whether to apply symbol mapping. Defaults to False.
        empty_error (str, optional): Error message for empty slug. Defaults to "Generated unique slug is empty.".
        long_error (str, optional): Error message for slug being too long. Defaults to "Generated unique slug is too long.".

    Returns:
        str: The generated unique slug.
    """

    # Get the field value
    field_value = getattr(instance, field_name)

    # Apply symbol mapping if requested
    if use_symbol_mapping:
        # Define symbol_mapping
        symbol_mapping = (
            # symbols
            (" ", "-"),
            ("!", ""),
            ('"', ""),
            ("#", ""),
            ("$", ""),
            ("%", ""),
            ("&", "and"),
            ("'", ""),
            ("(", ""),
            (")", ""),
            ("*", ""),
            ("+", ""),
            (",", ""),
            ("-", ""),
            (".", ""),
            ("/", ""),
            (":", ""),
            (";", ""),
            ("<", ""),
            ("=", ""),
            (">", ""),
            ("?", ""),
            ("@", "at"),
            ("[", ""),
            ("\\", ""),
            ("]", ""),
            ("^", ""),
            ("_", ""),
            ("`", ""),
            ("{", ""),
            ("|", ""),
            ("}", ""),
            ("~", ""),
            ("№", "no"),
            # Azerbaijani alphabet
            ("ç", "c"),
            ('ə', 'e'),
            ('ğ', 'g'),
            ("ı", "i"),
            ('İ', 'I'),
            ('ö', 'o'),
            ('ş', 's'),
            ('ü', 'u'),
        )

        # Replace symbols based on symbol_mapping
        for symbol, replacement in symbol_mapping:
            field_value = field_value.replace(symbol, replacement)

    # Apply slugify to the modified field value
    base_slug = slugify(field_value)
    unique_slug = base_slug
    counter = 1

    # Create a unique slug
    queryset = instance.__class__.objects.filter(slug=unique_slug)
    if instance.pk:
        queryset = queryset.exclude(pk=instance.pk)

    while queryset.exists():
        unique_slug = f"{base_slug}-{counter}"
        counter += 1
        queryset = instance.__class__.objects.filter(slug=unique_slug)

    if not unique_slug:
        raise ValueError(empty_error_msg)

    if max_length:
        if len(unique_slug) > max_length:
            raise ValueError(long_error_msg)

    return unique_slug
