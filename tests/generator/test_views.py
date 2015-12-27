import unittest

from appgen.generator.views import ViewsGenerator

from tests.models import Question


class ViewsGeneratorTests(unittest.TestCase):

    def test_generate_views_for_model_creates_form_code(self):
        expected = """from django.core.urlresolvers import reverse_lazy
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .forms import QuestionForm
from .models import Question


class QuestionList(ListView):
    model = Question


class QuestionDetail(DetailView):
    model = Question


class QuestionCreate(CreateView):
    model = Question
    form_class = QuestionForm
    success_url = reverse_lazy('tests:list')


class QuestionUpdate(UpdateView):
    model = Question
    form_class = QuestionForm
    success_url = reverse_lazy('tests:list')


class QuestionDelete(DeleteView):
    model = Question
    success_url = reverse_lazy('tests:list')
"""

        actual = ViewsGenerator(Question).generate()

        self.assertEqual(expected, actual)
