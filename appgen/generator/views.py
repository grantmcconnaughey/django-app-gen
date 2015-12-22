from appgen.generator import Generator


class ViewsGenerator(Generator):

    template_name = 'appgen/python/views.py'

    def get_extra_context(self):
        model_name = self.model_class.__name__
        model_import = 'from {} import {}'.format(self.model_class.__module__,
                                                  model_name)
        return {
            'model_import': model_import,
        }
