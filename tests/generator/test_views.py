import unittest

from appgen.generator.views import generate_views_for_model

from tests.models import Question


class ViewsGeneratorTests(unittest.TestCase):

    def test_generate_views_for_model_creates_form_code(self):
        expected = """from django.views.generic import TemplateView, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from tests.models import Question


class QuestionList(ListView):
    model = Question


class QuestionCreate(CreateView):
    model = Question
    fields = ('choice', 'id', 'question_text', 'pub_date', )


class QuestionUpdate(UpdateView):
    model = Question
    fields = ('choice', 'id', 'question_text', 'pub_date', )


class QuestionDelete(DeleteView):
    model = Question
"""

        actual = generate_views_for_model(Question)

        self.assertEqual(expected, actual)
