import os
import sys

from inkpy.tests import settings

# set DJANGO_SETTINGS_MODULE before Django is imported
os.environ['DJANGO_SETTINGS_MODULE'] = 'inkpy.tests.settings'


def run_tests(settings):
    import django
    from django.test.utils import get_runner

    if hasattr(django, 'setup'):
        django.setup()

    TestRunner = get_runner(settings)
    test_runner = TestRunner(interactive=False)
    failures = test_runner.run_tests(['inkpy'])
    return failures


def main():
    sys.exit(run_tests(settings))


if __name__ == '__main__':
    main()
