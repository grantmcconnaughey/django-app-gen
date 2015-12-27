import sys

from django.apps import apps
from django.core.management.base import BaseCommand, CommandError


class GeneratorCommand(BaseCommand):

    generators = []

    def add_arguments(self, parser):
        parser.add_argument('model', nargs='+', type=str,
                            help='The model name to generate files for.')

    def handle(self, *args, **options):
        model_name = options.get('model')[0]
        model_class = None

        matches = [model_class for model_class in apps.get_models()
                   if model_class.__name__ == model_name]

        if len(matches) == 1:
            model_class = matches[0]
        elif len(matches) > 1:
            msg = ('There are multiple models called {}. django-app-gen does '
                   'not handle multiple models with the same name '
                   '(yet).'.format(model_name))
            raise CommandError(msg)
        else:
            msg = ('There are no models called {}. Hint: Is your '
                   'app in INSTALLED_APPS?'.format(model_name))
            raise CommandError(msg)

        sys.stdout.write('Generating files...')

        for generator in self.generators:
            generator(model_class).generate_file()

        sys.stdout.write('Done!')
