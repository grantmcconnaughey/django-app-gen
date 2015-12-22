from django.apps import apps
from django.core.management import BaseCommand


from appgen.generator.forms import FormsGenerator
from appgen.generator.templates import *
from appgen.generator.tests import TestsGenerator
from appgen.generator.urls import URLsGenerator
from appgen.generator.views import ViewsGenerator


class Command(BaseCommand):
    help = "Generates views, templates, forms, URLs, and tests for a model."

    def add_arguments(self, parser):
        parser.add_argument('model', nargs='+', type=str)

    def handle(self, *args, **options):
        model_name = options.get('model')
        model_class = None

        matches = [model_class for model_class in apps.get_models()
                   if model_class.__name__ == model_name]

        if len(matches) == 1:
            model_class = matches[0]

        FormsGenerator(model_class).generate_file()
        CreateTemplateGenerator(model_class).generate_file()
        UpdateTemplateGenerator(model_class).generate_file()
        DetailTemplateGenerator(model_class).generate_file()
        DeleteTemplateGenerator(model_class).generate_file()
        ListTemplateGenerator(model_class).generate_file()
        FormTemplateGenerator(model_class).generate_file()
        TestsGenerator(model_class).generate_file()
        URLsGenerator(model_class).generate_file()
        ViewsGenerator(model_class).generate_file()
