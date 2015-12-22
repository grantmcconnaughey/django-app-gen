from appgen.management.commands.base import GeneratorCommand
from appgen.generator.forms import FormsGenerator
from appgen.generator.templates import *
from appgen.generator.tests import TestsGenerator
from appgen.generator.urls import URLsGenerator
from appgen.generator.views import ViewsGenerator


class Command(GeneratorCommand):
    help = "Generates views, templates, forms, URLs, and tests for a model."

    generators = [
        FormsGenerator, CreateTemplateGenerator, UpdateTemplateGenerator,
        DetailTemplateGenerator, DeleteTemplateGenerator,
        ListTemplateGenerator, FormTemplateGenerator, TestsGenerator,
        URLsGenerator, ViewsGenerator,
    ]
