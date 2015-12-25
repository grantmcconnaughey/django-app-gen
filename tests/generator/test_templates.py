import unittest

from appgen.generator.templates import *

from tests.models import Question


class TemplatesGeneratorTests(unittest.TestCase):

    def test_create_contains_header(self):
        result = CreateTemplateGenerator(Question).generate()

        self.assertIn('<h1>Create Question</h1>', result)

    def test_create_includes_form(self):
        result = CreateTemplateGenerator(Question).generate()

        self.assertIn("{% include 'appgen/html/_form.html' %}", result)

    def test_update_contains_header(self):
        result = UpdateTemplateGenerator(Question).generate()

        self.assertIn('<h1>Update Question</h1>', result)

    def test_update_includes_form(self):
        result = UpdateTemplateGenerator(Question).generate()

        self.assertIn("{% include 'appgen/html/_form.html' %}", result)

    def test_detail_contains_header(self):
        result = DetailTemplateGenerator(Question).generate()

        self.assertIn("<h1>{{ object }}</h1>", result)

    def test_detail_has_field_labels(self):
        result = DetailTemplateGenerator(Question).generate()

        self.assertIn('<span id="id-label" class="property-label">Id</span>', result)
        self.assertIn('<span id="choice-label" class="property-label">Choice</span>', result)
        self.assertIn('<span id="question_text-label" class="property-label">Question_text</span>',
                      result)
        self.assertIn('<span id="pub_date-label" class="property-label">Pub_date</span>', result)

    def test_detail_has_field_values(self):
        result = DetailTemplateGenerator(Question).generate()

        self.assertIn('<span aria-labelledby="id-label" class="property-value">{{ object.id }}</span>', result)
        self.assertIn('<span aria-labelledby="choice-label" class="property-value">{{ object.choice }}</span>', result)
        self.assertIn('<span aria-labelledby="question_text-label" class="property-value">{{ object.question_text }}</span>', result)
        self.assertIn('<span aria-labelledby="pub_date-label" class="property-value">{{ object.pub_date }}</span>', result)

    def test_delete_has_form(self):
        result = DeleteTemplateGenerator(Question).generate()

        self.assertIn('<form action="" method="post" class="question-form">',
                      result)

    def test_delete_has_confirmation_message(self):
        result = DeleteTemplateGenerator(Question).generate()

        self.assertIn('<form action="" method="post" class="question-form">',
                      result)

    def test_delete_has_csrf_token(self):
        result = DeleteTemplateGenerator(Question).generate()

        self.assertIn('{% csrf_token %}', result)

    def test_delete_has_submit_button(self):
        result = DeleteTemplateGenerator(Question).generate()

        self.assertIn('<input type="submit" value="Submit"></input>', result)

    def test_list_has_header(self):
        result = ListTemplateGenerator(Question).generate()

        self.assertIn('<h1>Question List</h1>', result)

    def test_list_has_table(self):
        result = ListTemplateGenerator(Question).generate()

        self.assertIn('<table class="question-table">', result)

    def test_list_has_headers(self):
        result = ListTemplateGenerator(Question).generate()

        self.assertIn('<th>Id</th>', result)
        self.assertIn('<th>Choice</th>', result)
        self.assertIn('<th>Question Text</th>', result)
        self.assertIn('<th>Pub Date</th>', result)

    def test_list_has_data(self):
        result = ListTemplateGenerator(Question).generate()

        self.assertIn('<td>{{ object.id }}</td>', result)
        self.assertIn('<td>{{ object.choice }}</td>', result)
        self.assertIn('<td>{{ object.question_text }}</td>', result)
        self.assertIn('<td>{{ object.pub_date }}</td>', result)

    def test_list_loops_through_object_list(self):
        result = ListTemplateGenerator(Question).generate()

        self.assertIn('{% for object in object_list %}', result)

    def test_form_contains_form_html(self):
        result = FormTemplateGenerator(Question).generate()

        self.assertIn('<form action="" method="post" class="question-form">',
                      result)

    def test_form_outputs_form_as_paragraph(self):
        result = FormTemplateGenerator(Question).generate()

        self.assertIn('{{ form.as_p }}', result)

    def test_form_has_csrf_token(self):
        result = FormTemplateGenerator(Question).generate()

        self.assertIn('{% csrf_token %}', result)

    def test_form_has_submit_button(self):
        result = FormTemplateGenerator(Question).generate()

        self.assertIn('<input type="submit" value="Submit"></input>', result)
