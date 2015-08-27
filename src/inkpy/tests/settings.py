import django

DEBUG = False

SECRET_KEY = 'SECRET_KEY'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
        'TEST_NAME': ':memory:',
    },
}

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.admin',
    'django.contrib.messages',

    'inkpy',
]

if django.VERSION < (1, 8):
    TEST_RUNNER = 'django.test.simple.DjangoTestSuiteRunner'
else:
    TEST_RUNNER = 'django.test.runner.DiscoverRunner'

LANGUAGE_CODE = 'en-us'

ROOT_URLCONF = ''

SITE_ID = 1
