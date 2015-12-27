=============================
django-app-gen
=============================

.. image:: https://readthedocs.org/projects/django-app-gen/badge/?version=latest
    :target: http://django-app-gen.readthedocs.org/en/latest/?badge=latest
    :alt: Documentation Status

.. image:: https://travis-ci.org/grantmcconnaughey/django-app-gen.svg?branch=master
    :target: https://travis-ci.org/grantmcconnaughey/django-app-gen

.. image:: https://coveralls.io/repos/grantmcconnaughey/django-app-gen/badge.svg?branch=master&service=github
  :target: https://coveralls.io/github/grantmcconnaughey/django-app-gen?branch=master

Generate CRUD views, templates, forms, URLs, and tests for a model. For Django 1.8+ and Python 2.7/3.3+.

Documentation
-------------

The full documentation is at https://django-app-gen.readthedocs.org.

Quickstart
----------

Install django-app-gen::

    pip install django-app-gen

Create a model in your app's models.py file::

    from django.db import models


    class Question(models.Model):
        question_text = models.CharField(max_length=200)
        pub_date = models.DateTimeField('date published')

Then generate your views, templates, forms, URLs, and tests.::

    python manage.py generate_all Question

Running Tests
--------------

Does the code actually work?

::

    source <YOURVIRTUALENV>/bin/activate
    (myenv) $ pip install -r requirements-text.txt
    (myenv) $ python runtests.py

Credits
---------

Tools used in rendering this package:

*  Cookiecutter_
*  `cookiecutter-pypackage`_

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`cookiecutter-pypackage`: https://github.com/pydanny/cookiecutter-djangopackage
