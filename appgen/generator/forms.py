from appgen.generator import Generator


class FormsGenerator(Generator):

    template_name = 'appgen/python/forms.py'

    def get_extra_context(self):
        model_name = self.model_class.__name__
        model_import = 'from {} import {}'.format(self.model_class.__module__,
                                                  model_name)
        return {
            'model_import': model_import,
        }
