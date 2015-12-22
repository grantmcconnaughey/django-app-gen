import unittest

from appgen.generator.templates import generate_form_template

from tests.models import Question


class TemplatesGeneratorTests(unittest.TestCase):

    def test_form_contains_form_html(self):
        result = generate_form_template(Question)

        self.assertIn('<form action="" method="post" class="question-form">',
                      result)

    def test_form_outputs_form_as_paragraph(self):
        result = generate_form_template(Question)

        self.assertIn('{{ form.as_p }}', result)

    def test_form_uses_csrf_token(self):
        result = generate_form_template(Question)

        self.assertIn('{% csrf_token %}', result)

    def test_form_has_submit_button(self):
        result = generate_form_template(Question)

        self.assertIn('<input type="submit" value="Submit"></input>', result)
