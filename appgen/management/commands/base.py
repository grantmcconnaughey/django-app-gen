from django.apps import apps
from django.core.management import BaseCommand


class GeneratorCommand(BaseCommand):

    generators = []

    def add_arguments(self, parser):
        parser.add_argument('model', nargs='+', type=str)

    def handle(self, *args, **options):
        model_name = options.get('model')
        model_class = None

        matches = [model_class for model_class in apps.get_models()
                   if model_class.__name__ == model_name]

        if len(matches) == 1:
            model_class = matches[0]

        for generator in self.generators:
            generator(model_class).generate_file()
