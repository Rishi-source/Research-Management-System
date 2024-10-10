from django import template

register = template.Library()

@register.filter(name='subtract')
def subtract(value, arg):
    """Subtracts the arg from the value."""
    try:
        return int(value) - int(arg)
    except (ValueError, TypeError):
        return value  # or you could choose to return 0 or an error message
