import unittest

from appgen.generator.forms import FormsGenerator

from tests.models import Question


class FormsGeneratorTests(unittest.TestCase):

    def test_generate_form_for_model_creates_form_code(self):
        expected = """from django import forms

from tests.models import Question


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ('choice', 'id', 'question_text', 'pub_date', )
"""

        actual = FormsGenerator(Question).generate()

        self.assertEqual(expected, actual)
