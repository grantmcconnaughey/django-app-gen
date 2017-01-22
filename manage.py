#!/usr/bin/env python
import os
import sys




try:
    from django.conf import settings
    from django.test.utils import get_runner

    
    
    settings.configure(
        DEBUG=True,
        USE_TZ=True,
        DATABASES={
            "default": {
                "ENGINE": "django.db.backends.sqlite3",
            }
        },
        ROOT_URLCONF="tests.urls",
        INSTALLED_APPS=[
            "django.contrib.auth",
            "django.contrib.contenttypes",
            "django.contrib.sites",
            "appgen",
            "tests",
        ],
        SITE_ID=1,
        MIDDLEWARE_CLASSES=(),
    )

    
    
    try:
        import django
        
        
        setup = django.setup
    except AttributeError:
        pass
    else:
        setup()

except ImportError:
    import traceback
    traceback.print_exc()
    raise ImportError("To fix this error, run: pip install -r requirements-test.txt")


    
    
if __name__ == "__main__":
    sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

    
    
    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)

    
    
    
