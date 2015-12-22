from django.template.loader import render_to_string


class Generator(object):

    def __init__(self, model_class=None):
        self.model_class = model_class

    def generate(self):
        return render_to_string(self.get_template_name(), self.get_context())

    def get_context(self):
        context = {
            'model_name': self.model_class.__name__,
            'field_names': [f.name for f in self.model_class._meta.get_fields()],
        }
        context.update(self.get_extra_context())
        return context

    def get_extra_context(self):
        return {}

    def get_template_name(self):
        return self.template_name
