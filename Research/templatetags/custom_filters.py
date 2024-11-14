from django import template

register = template.Library()


@register.filter
def get_range(value):
    """
    Returns a range of numbers up to the given value.
    Example: {% for i in 6|get_range %}
    """
    return range(value)
