import unittest

from appgen.generator.tests import TestsGenerator

from tests.models import Question


class TestsGeneratorTests(unittest.TestCase):

    def test_method_names(self):
        result = TestsGenerator(Question).generate()

        self.assertIn('test_create_get', result)
        self.assertIn('test_create_post_creates_question', result)
        self.assertIn('test_update_get', result)
        self.assertIn('test_update_post_updates_question', result)
        self.assertIn('test_detail_get', result)
        self.assertIn('test_list_get', result)
        self.assertIn('test_delete_get', result)
        self.assertIn('test_delete_post_deletes_question', result)
