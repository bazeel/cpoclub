import os
import sys

import django.conf.global_settings as DEFAULT_SETTINGS

TEMPLATE_CONTEXT_PROCESSORS = DEFAULT_SETTINGS.TEMPLATE_CONTEXT_PROCESSORS + (
    'core.context_processors.user',
    'django.core.context_processors.request'
)

BASE_DIR = os.path.dirname(__file__)


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '+eo^)zvy2(pwdg6o5eh7%j@6cil8y2%%$=)2yj&o6@&eriw0!f'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'grappelli',
    'filebrowser',
    'tinymce',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'easy_thumbnails',

    'account',
    'core',
    'blog',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'urls'

WSGI_APPLICATION = 'wsgi.application'

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

TIME_ZONE = 'Europe/Moscow'
LANGUAGE_CODE = 'ru'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

PROJECT_ROOT = os.path.normpath(os.path.abspath(BASE_DIR))

MEDIA_ROOT = os.path.join(PROJECT_ROOT, 'media')

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = '/media/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = os.path.join(PROJECT_ROOT, 'static_root')



STATIC_URL = '/static/'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

GRAPPELLI_ADMIN_TITLE = 'cpoclub.ru'

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'django.contrib.staticfiles.finders.FileSystemFinder',
)



TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'templates'),
)

APPS_ROOT = os.path.join(BASE_DIR, 'apps')
sys.path.append(APPS_ROOT)


TINYMCE_DEFAULT_CONFIG = {
    'convert_urls': False,
    'height': '350',
    'theme': 'advanced',
    'plugins': 'advimage,advlink,fullscreen,media,safari,table',
    'theme_advanced_toolbar_location': 'top',
    'theme_advanced_buttons1': 'fullscreen,|,bold,italic,underline,' \
                               'strikethrough,|,justifyleft,justifycenter,' \
                               'justifyright,justifyfull,|,styleselect,' \
                               'formatselect,fontselect,fontsizeselect',
    'theme_advanced_buttons2': 'cut,copy,paste,pastetext,pasteword,|,' \
                               'bullist,numlist,|,outdent,indent,' \
                               'blockquote,|,undo,redo,|,link,unlink,' \
                               'anchor,image,cleanup,help,code,|,' \
                               'forecolor,backcolor',
    'theme_advanced_buttons3': 'tablecontrols,|,hr,removeformat,visualaid,' \
                               '|,sub,sup,|,charmap,media',
    'theme_advanced_toolbar_align': 'center',
    'theme_advanced_statusbar_location': 'bottom',
    'theme_advanced_resizing': 'true',
    'extended_valid_elements': 'noindex',
    'file_browser_callback': "DjangoFileBrowser",
}



FILEBROWSER_DIRECTORY = ''
#APPEND_SLASH = False

from ignored_settings import *