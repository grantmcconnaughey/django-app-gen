import unittest

from appgen.generator.templates import *

from tests.models import Question


class TemplatesGeneratorTests(unittest.TestCase):

    def test_create_contains_header(self):
        result = generate_create_template(Question)

        self.assertIn('<h1>Create Question</h1>', result)

    def test_create_includes_form(self):
        result = generate_create_template(Question)

        self.assertIn("{% include 'appgen/html/_form.html' %}", result)

    def test_update_contains_header(self):
        result = generate_update_template(Question)

        self.assertIn('<h1>Update Question</h1>', result)

    def test_update_includes_form(self):
        result = generate_update_template(Question)

        self.assertIn("{% include 'appgen/html/_form.html' %}", result)

    def test_delete_has_form(self):
        result = generate_delete_template(Question)

        self.assertIn('<form action="" method="post" class="question-form">',
                      result)

    def test_delete_has_confirmation_message(self):
        result = generate_delete_template(Question)

        self.assertIn('<form action="" method="post" class="question-form">',
                      result)

    def test_delete_has_csrf_token(self):
        result = generate_delete_template(Question)

        self.assertIn('{% csrf_token %}', result)

    def test_delete_has_submit_button(self):
        result = generate_delete_template(Question)

        self.assertIn('<input type="submit" value="Submit"></input>', result)

    def test_form_contains_form_html(self):
        result = generate_form_template(Question)

        self.assertIn('<form action="" method="post" class="question-form">',
                      result)

    def test_form_outputs_form_as_paragraph(self):
        result = generate_form_template(Question)

        self.assertIn('{{ form.as_p }}', result)

    def test_form_has_csrf_token(self):
        result = generate_form_template(Question)

        self.assertIn('{% csrf_token %}', result)

    def test_form_has_submit_button(self):
        result = generate_form_template(Question)

        self.assertIn('<input type="submit" value="Submit"></input>', result)
