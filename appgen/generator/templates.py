from appgen.generator import Generator


class CreateTemplateGenerator(Generator):

    template_name = 'appgen/html/create.html'
    file_name = 'create.html'


class UpdateTemplateGenerator(Generator):

    template_name = 'appgen/html/update.html'
    file_name = 'update.html'


class DetailTemplateGenerator(Generator):

    template_name = 'appgen/html/detail.html'
    file_name = 'detail.html'


class DeleteTemplateGenerator(Generator):

    template_name = 'appgen/html/delete.html'
    file_name = 'delete.html'


class ListTemplateGenerator(Generator):

    template_name = 'appgen/html/list.html'
    file_name = 'list.html'


class FormTemplateGenerator(Generator):

    template_name = 'appgen/html/_form.html'
    file_name = '_form.html'
