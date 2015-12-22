from django import template

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
