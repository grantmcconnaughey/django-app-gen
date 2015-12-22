import unittest

from appgen.templatetags import appgen_tags


class TemplateTagTests(unittest.TestCase):

    def test_start_tag(self):
        self.assertEqual(appgen_tags.start_tag(), '{%')

    def test_end_tag(self):
        self.assertEqual(appgen_tags.end_tag(), '%}')

    def test_start_var(self):
        self.assertEqual(appgen_tags.start_var(), '{{')

    def test_end_var(self):
        self.assertEqual(appgen_tags.end_var(), '}}')
