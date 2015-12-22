from appgen.utils import render_template


def generate_create_template(model_class,
                             template_name='appgen/html/create.html'):
    context = {'model_name': model_class.__name__}
    return render_template(template_name, context)


def generate_update_template(model_class,
                             template_name='appgen/html/update.html'):
    context = {'model_name': model_class.__name__}
    return render_template(template_name, context)


def generate_detail_template(model_class,
                             template_name='appgen/html/detail.html'):
    context = {'model_name': model_class.__name__}
    return render_template(template_name, context)


def generate_delete_template(model_class,
                             template_name='appgen/html/delete.html'):
    context = {'model_name': model_class.__name__}
    return render_template(template_name, context)


def generate_list_template(model_class,
                           template_name='appgen/html/list.html'):
    context = {
        'model_name': model_class.__name__,
        'field_names': [f.name for f in model_class._meta.get_fields()],
    }
    return render_template(template_name, context)


def generate_form_template(model_class,
                           template_name='appgen/html/_form.html'):
    context = {'model_name': model_class.__name__}
    return render_template(template_name, context)
