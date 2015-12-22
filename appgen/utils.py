from django.template.loader import render_to_string


def render_template(template_name, context=None):
    if context is None:
        context = {}
    return render_to_string(template_name, context)
