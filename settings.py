# Initialize App Engine and import the default settings (DB backend, etc.).
# If you want to use a different backend you have to remove all occurences
# of "djangoappengine" from this file.
from djangoappengine.settings_base import *

import os

SECRET_KEY = '=r-skhe$*#Jdksh#*DHdhfsk9q(#*47hfkLdkh29dh8hdJShz'

INSTALLED_APPS = (
#    'django.contrib.admin',
    'django.contrib.contenttypes',
    'django.contrib.auth',
    'django.contrib.sessions',
    'django.contrib.admin',
    'djangotoolbox',
	'autoload',
	'dbindexer',
    'schedule',
    'users',
	'registration',

    # djangoappengine should come last, so it can override a few manage.py commands
    'djangoappengine',
)

MIDDLEWARE_CLASSES = (
	'autoload.middleware.AutoloadMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
	
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.request',
    'django.core.context_processors.media',
)

# This test runner captures stdout and associates tracebacks with their
# corresponding output. Helps a lot with print-debugging.
TEST_RUNNER = 'djangotoolbox.test.CapturingTestSuiteRunner'

ADMIN_MEDIA_PREFIX = '/media/admin/'
TEMPLATE_DIRS = (os.path.join(os.path.dirname(__file__), 'templates'),)

ROOT_URLCONF = 'urls'

AUTOLOAD_SITECONF = 'dbindexes'

SUBJECTS = (
	(1, "Algebra 1"),
	(2, "Algebra 2"),
	(3, "Calculus"),
	(4, "Trigonometry"),
	(5, "Math Analysis"),
)

LOGIN_URL = '/account/login'
LOGIN_REDIRECT_URL = '/me'
REGISTER_SUCCESS_URL = LOGIN_REDIRECT_URL

DATABASES = {
    'default': {
        'ENGINE': 'dbindexer',
        'TARGET': 'gae',
    },
    'gae': {
        'ENGINE': 'djangoappengine.db',
    },
}
