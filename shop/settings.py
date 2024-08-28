"""
Django settings for shop project.

Generated by 'django-admin startproject' using Django 4.1.3.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

from pathlib import Path
import os
from django.contrib.messages import constants as messages

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-)g76giif9kp^quh^+93hhu1+r2h6hj+&-1(os7*1x*!#u9s(z@'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*', '']

# CKEDITOR_UPLOAD_PATH = "uploads/"


# Application definition

INSTALLED_APPS = [
    'material',
    'material.admin',
    # 'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_ckeditor_5',
    'tinymce',
    'nfs.apps.NfsConfig',
    'ckeditor',
    # 'ckeditor_uploader',
]

AUTH_USER_MODEL = 'nfs.CustomUser'

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
]

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'root': {
        'handlers': ['console'],
        'level': 'DEBUG',
    },
}

# CSRF_TRUSTED_ORIGINS = ['https://39da-152-59-143-128.ngrok-free.app/']


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

]



ROOT_URLCONF = 'shop.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR / "templates"),],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]




WSGI_APPLICATION = 'shop.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}



# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]



# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST='smtp.gmail.com'
# EMAIL_USE_TLS= True
EMAIL_PORT= 465
EMAIL_HOST_USER="nafishcommunication10@gmail.com"
EMAIL_HOST_PASSWORD="yanl uoez ptbn jyes"
EMAIL_USE_TLS= True






CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': [
            {'name': 'document', 'items': ['Source', '-', 'Save', 'NewPage', 'Preview', 'Print', '-', 'Templates']},
            {'name': 'clipboard', 'items': ['Cut', 'Copy', 'Paste', 'PasteText', 'PasteFromWord', '-', 'Undo', 'Redo']},
            {'name': 'editing', 'items': ['Find', 'Replace', '-', 'SelectAll', '-', 'Scayt']},
            {'name': 'forms', 'items': ['Form', 'Checkbox', 'Radio', 'TextField', 'Textarea', 'Select', 'Button', 'ImageButton', 'HiddenField']},
            '/',
            {'name': 'basicstyles', 'items': ['Bold', 'Italic', 'Underline', 'Strike', 'Subscript', 'Superscript', '-', 'RemoveFormat']},
            {'name': 'paragraph', 'items': ['NumberedList', 'BulletedList', '-', 'Outdent', 'Indent', '-', 'Blockquote', 'CreateDiv', '-', 'JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock', '-', 'BidiLtr', 'BidiRtl', 'Language']},
            {'name': 'links', 'items': ['Link', 'Unlink', 'Anchor']},
            {'name': 'insert', 'items': ['Image', 'Table', 'HorizontalRule', 'Smiley', 'SpecialChar', 'PageBreak', 'Iframe']},
            '/',
            {'name': 'styles', 'items': ['Styles', 'Format', 'Font', 'FontSize']},
            {'name': 'colors', 'items': ['TextColor', 'BGColor']},
            {'name': 'tools', 'items': ['Maximize', 'ShowBlocks']},
            {'name': 'about', 'items': ['About']}
        ],
        'height': 300,
        'width': '100%',
        'extraPlugins': ','.join([
            'uploadimage',  # the upload image feature
            'image2',  # the 'image2' plugin (replace the default 'image' plugin)
            'table',  # table plugin
            'tabletools',  # additional table tools
        ]),
    },
}



# CKEDITOR_5_CONFIGS = {
#     'extends': {
#         'blockToolbar': [
#             'paragraph', 'heading1', 'heading2', 'heading3',
#             '|',
#             'bulletedList', 'numberedList',
#             '|',
#             'blockQuote'
#         ],
#         'toolbar': [
#             'heading', '|', 'outdent', 'indent', '|', 'bold', 'italic', 'link', 'underline', 'strikethrough',
#             'code', 'subscript', 'superscript', 'highlight', '|', 'codeBlock', 'sourceEditing', 'insertImage',
#             'bulletedList', 'numberedList', 'todoList', '|', 'blockQuote', 'imageUpload', '|',
#             'fontSize', 'fontFamily', 'fontColor', 'fontBackgroundColor', 'mediaEmbed', 'removeFormat',
#             'insertTable'
#         ],
#         'link': {
#             'target': ['_blank' ] # Ensure links open in a new tab
#         },
#         'image': {
#             'toolbar': [
#                 'imageTextAlternative', '|', 'imageStyle:alignLeft',
#                 'imageStyle:alignRight', 'imageStyle:alignCenter', 'imageStyle:side', '|'
#             ],
#             'styles': [
#                 'full',
#                 'side',
#                 'alignLeft',
#                 'alignRight',
#                 'alignCenter'
#             ]
#         },
#         'table': {
#             'contentToolbar': [
#                 'tableColumn', 'tableRow', 'mergeTableCells',
#                 'tableProperties', 'tableCellProperties'
#             ],
#             'tableProperties': {
#                 'borderColors': 'customColorPalette',
#                 'backgroundColors': 'customColorPalette'
#             },
#             'tableCellProperties': {
#                 'borderColors': 'customColorPalette',
#                 'backgroundColors': 'customColorPalette'
#             }
#         },
#         'heading': {
#             'options': [
#                 { 'model': 'paragraph', 'title': 'Paragraph', 'class': 'ck-heading_paragraph' },
#                 { 'model': 'heading1', 'view': 'h1', 'title': 'Heading 1', 'class': 'ck-heading_heading1' },
#                 { 'model': 'heading2', 'view': 'h2', 'title': 'Heading 2', 'class': 'ck-heading_heading2' },
#                 { 'model': 'heading3', 'view': 'h3', 'title': 'Heading 3', 'class': 'ck-heading_heading3' }
#             ]
#         }
#     },
#     'list': {
#         'properties': {
#             'styles': 'true',
#             'startIndex': 'true',
#             'reversed': 'true'
#         }
#     }
# }



MATERIAL_ADMIN_SITE = {
    'HEADER': 'Online Duniya Admin Panel',
    # Other settings...
}


ACCESS_TOKEN = 'EAAf1ivuiZAZCcBOz5nHREnXSJrw6lFCZCBShi4hzePyL6MUh6Xop6ZCrKj0ksCK1iNYpZCACoZAR6jWrpNIZB1KS8fK58EO3c7bZA8Az1ZBCEFBbnvHXxdL9ZB8ghYW4S5pOYUZCF2jQLWIzQMBh4HMjmkkmUSV7LQykLlIzvB9JSinGSZCqKjWqCGLKX7ai6bEW2P3Kht9qRjODwQa6ZBr8ZA42nyaY2WkKNDnFyCqisZD'
PHONE_NUMBER_ID = '382615361607149'