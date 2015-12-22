from appgen.utils import render_template


def generate_form_for_model(model_class,
                            template_name='appgen/python/forms.py'):
    """
    Returns a string containing the generated forms.py code for a given model
    class.
    """
    model_name = model_class.__name__
    model_import = 'from {} import {}'.format(model_class.__module__,
                                              model_name)
    context = {
        'model_name': model_name,
        'model_import': model_import,
        'field_names': [f.name for f in model_class._meta.get_fields()],
    }
    return render_template(template_name, context)
