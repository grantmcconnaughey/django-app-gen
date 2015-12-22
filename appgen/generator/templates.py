from appgen.utils import render_template


def generate_create_template(model_class,
                             template_name='appgen/html/create.html'):
    context = {}
    return render_template(template_name, context)


def generate_update_template(model_class,
                             template_name='appgen/html/update.html'):
    context = {}
    return render_template(template_name, context)


def generate_detail_template(model_class,
                             template_name='appgen/html/detail.html'):
    context = {}
    return render_template(template_name, context)


def generate_delete_template(model_class,
                             template_name='appgen/html/delete.html'):
    context = {}
    return render_template(template_name, context)


def generate_list_template(model_class,
                           template_name='appgen/html/list.html'):
    context = {}
    return render_template(template_name, context)


def generate_form_template(model_class,
                           template_name='appgen/html/_form.html'):
    context = {}
    return render_template(template_name, context)
