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

    def test_table_header_strips_spaces(self):
        self.assertEqual(appgen_tags.table_header(' Hello World '),
                         'Hello World')

    def test_table_header_replaces_underscores_with_spaces(self):
        self.assertEqual(appgen_tags.table_header('Hello_World'),
                         'Hello World')

    def test_table_header_converts_to_titlecase(self):
        self.assertEqual(appgen_tags.table_header('hello_world'),
                         'Hello World')

    def test_table_header_converts_objects_to_strs(self):
        class TestObj(object):
            name = "hello_world"

            def __unicode__(self):
                return self.name

        obj = TestObj()

        self.assertEqual(appgen_tags.table_header(obj),
                         'Hello World')
