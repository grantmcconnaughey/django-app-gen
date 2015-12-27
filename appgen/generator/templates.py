from appgen.generator import Generator


class TemplateGeneratorMixin(object):

    def get_file_name(self):
        return 'templates/{}/{}'.format(self.app_label, self.file_name)


class CreateTemplateGenerator(TemplateGeneratorMixin, Generator):

    template_name = 'appgen/html/create.html'
    file_name = 'create.html'


class UpdateTemplateGenerator(TemplateGeneratorMixin, Generator):

    template_name = 'appgen/html/update.html'
    file_name = 'update.html'


class DetailTemplateGenerator(TemplateGeneratorMixin, Generator):

    template_name = 'appgen/html/detail.html'
    file_name = 'detail.html'


class DeleteTemplateGenerator(TemplateGeneratorMixin, Generator):

    template_name = 'appgen/html/delete.html'
    file_name = 'delete.html'


class ListTemplateGenerator(TemplateGeneratorMixin, Generator):

    template_name = 'appgen/html/list.html'
    file_name = 'list.html'


class FormTemplateGenerator(TemplateGeneratorMixin, Generator):

    template_name = 'appgen/html/_form.html'
    file_name = '_form.html'
