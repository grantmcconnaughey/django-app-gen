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

    def test_detail_contains_header(self):
        result = generate_detail_template(Question)

        self.assertIn("<h1>{{ object }}</h1>", result)

    def test_detail_has_field_labels(self):
        result = generate_detail_template(Question)

        self.assertIn('<span id="id-label" class="property-label">Id</span>', result)
        self.assertIn('<span id="choice-label" class="property-label">Choice</span>', result)
        self.assertIn('<span id="question_text-label" class="property-label">Question_text</span>',
                      result)
        self.assertIn('<span id="pub_date-label" class="property-label">Pub_date</span>', result)

    def test_detail_has_field_values(self):
        result = generate_detail_template(Question)

        self.assertIn('<span aria-labelledby="id-label" class="property-value">{{ object.id }}</span>', result)
        self.assertIn('<span aria-labelledby="choice-label" class="property-value">{{ object.choice }}</span>', result)
        self.assertIn('<span aria-labelledby="question_text-label" class="property-value">{{ object.question_text }}</span>', result)
        self.assertIn('<span aria-labelledby="pub_date-label" class="property-value">{{ object.pub_date }}</span>', result)

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

    def test_list_has_header(self):
        result = generate_list_template(Question)

        self.assertIn('<h1>Question List</h1>', result)

    def test_list_has_table(self):
        result = generate_list_template(Question)

        self.assertIn('<table class="question-table">', result)

    def test_list_has_headers(self):
        result = generate_list_template(Question)

        self.assertIn('<th>Id</th>', result)
        self.assertIn('<th>Choice</th>', result)
        self.assertIn('<th>Question_text</th>', result)
        self.assertIn('<th>Pub_date</th>', result)

    def test_list_has_data(self):
        result = generate_list_template(Question)

        self.assertIn('<td>{{ object.id }}</td>', result)
        self.assertIn('<td>{{ object.choice }}</td>', result)
        self.assertIn('<td>{{ object.question_text }}</td>', result)
        self.assertIn('<td>{{ object.pub_date }}</td>', result)

    def test_list_loops_through_object_list(self):
        result = generate_list_template(Question)

        self.assertIn('{% for object in object_list %}', result)

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
