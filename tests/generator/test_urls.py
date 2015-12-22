import unittest

from appgen.generator.urls import URLsGenerator

from tests.models import Question


class URLsGeneratorTests(unittest.TestCase):

    def test_url_generator(self):
        expected = """from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$', views.QuestionList.as_view(), name='list'),
    url(r'^new/$', views.QuestionCreate.as_view(), name='create'),
    url(r'^(?P<pk>\d+)/$', views.QuestionDetail.as_view(), name='detail'),
    url(r'^(?P<pk>\d+)/update/$', views.QuestionUpdate.as_view(), name='update'),
    url(r'^(?P<pk>\d+)/delete/$', views.QuestionDelete.as_view(), name='delete'),
]
"""
        result = URLsGenerator(Question).generate()

        self.assertEqual(expected, result)
