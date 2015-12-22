from appgen.generator import Generator


class CreateTemplateGenerator(Generator):

    template_name = 'appgen/html/create.html'


class UpdateTemplateGenerator(Generator):

    template_name = 'appgen/html/update.html'


class DetailTemplateGenerator(Generator):

    template_name = 'appgen/html/detail.html'


class DeleteTemplateGenerator(Generator):

    template_name = 'appgen/html/delete.html'


class ListTemplateGenerator(Generator):

    template_name = 'appgen/html/list.html'


class FormTemplateGenerator(Generator):

    template_name = 'appgen/html/_form.html'
