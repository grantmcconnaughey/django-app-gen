from appgen.generator import Generator


class TestsGenerator(Generator):

    template_name = 'appgen/python/tests.py'

    def get_extra_context(self):
        model_name = self.model_class.__name__
        model_import = 'from {} import {}'.format(self.model_class.__module__,
                                                  model_name)
        return {
            'model_import': model_import,
            'list_url': '{}:list'.format(self.app_label),
            'create_url': '{}:create'.format(self.app_label),
            'detail_url': '{}:detail'.format(self.app_label),
            'update_url': '{}:update'.format(self.app_label),
            'delete_url': '{}:delete'.format(self.app_label),
        }
