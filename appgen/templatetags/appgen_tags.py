from django import template
from django.utils.encoding import force_text

register = template.Library()


@register.simple_tag
def start_tag():
    return '{%'


@register.simple_tag
def end_tag():
    return '%}'


@register.simple_tag
def start_var():
    return '{{'


@register.simple_tag
def end_var():
    return '}}'


@register.filter()
def table_header(value):
    """
    Strips spaces from a header, replaces underscores with spaces, and converts
    header to title-case.
    """
    return force_text(value).strip().replace('_', ' ').title()
