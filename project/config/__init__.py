from __future__ import absolute_import
import os
from os.path import join
from configurations import values

# for scheduling feed downloads and other asks using django-celery library
import djcelery
djcelery.setup_loader()




# This will make sure the app is always imported when
# Django starts so that shared_task will use this app.
from .celery import app as celery_app


BASE_DIR = os.path.dirname(os.path.dirname(__file__))


class Base(object):
    ALLOWED_HOSTS = []
    DEBUG = values.BooleanValue(True)
    TEMPLATE_DEBUG = values.BooleanValue(DEBUG)
    ROOT_URLCONF = "config.urls"
    SECRET_KEY = "9873KETNOEXA2121A"
    SITE_ID = 1
    # Python dotted path to the WSGI application used by Django"s runserver.
    WSGI_APPLICATION = "config.wsgi.application"

    #### Package: django-constance settings.
    # See: https://github.com/comoga/django-constance
    CONSTANCE_BACKEND = "constance.backends.redisd.RedisBackend"  # using Redis (default)
    CONSTANCE_REDIS_CONNECTION = "redis://vagrant:vagrant@localhost:6379/0"
    CONSTANCE_CONFIG = {
        "HOME_MESSAGE": ("This is a configurable setting via the admin", "The Default message shown on the home page."),
        "SYSTEM_EMAIL_ENQUIRY": ("enquiries@productfinder.com", "Email for General Enquiries"),
        "SYSTEM_EMAIL_SUPPORT": ("support@productfinder.com", "Email for Customer Support"),
    }
    #### End Package: django-constance settings.

    #### Package: django-celery settings
    # See: http://rapidsms.readthedocs.org/en/0.16.0/topics/celery.html
    # BROKER_URL = "redis://vagrant:vagrant@localhost:6379/0"
    BROKER_URL = 'amqp://guest:guest@localhost:5672//'
    # CELERY_IGNORE_RESULT = True
    CELERYBEAT_SCHEDULER = "djcelery.schedulers.DatabaseScheduler"
    CELERY_TIMEZONE = "Europe/London"
    CELERY_ENABLE_UTC = True

    # store AsyncResult in redis
    CELERY_RESULT_BACKEND = "redis"
    REDIS_HOST = "localhost"
    REDIS_PORT = 6379
    REDIS_DB = "0"
    REDIS_VHOST = "0" # have to check
    REDIS_USER="vagrant"
    REDIS_PASSWORD="vagrant"
    BROKER_TRANSPORT_OPTIONS = {'visibility_timeout': 3600}
    # CELERY_TASK_RESULT_EXPIRES =  3600
    CELERY_TASK_RESULT_EXPIRES = None
    REDIS_CONNECT_RETRY = True
    CELERY_SEND_EVENTS=True
    # CELERY_ACKS_LATE = True
    # REDIS_CONNECT_RETRY = True
    # CELERY_DISABLE_RATE_LIMITS = True
    #### End Package: django-celery settings


class Apps(object):
    # django apps
    DJANGO_APPS = (
        "django.contrib.admin",
        "django.contrib.auth",
        "django.contrib.contenttypes",
        "django.contrib.sessions",
        "django.contrib.sites",
        "django.contrib.messages",
        "django.contrib.staticfiles",
        "django.contrib.humanize",
        "django.contrib.webdesign",
    )
    # third party apps
    THIRD_PARTY_APPS = (
        "allauth",  # registration
        "allauth.account",  # registration
        "allauth.socialaccount",  # registration
        "constance",  # dynamic settings
        "crispy_forms",  # form layouts
        "floppyforms",  # html5 forms
        "django_extensions",  # simple useful extensions
        "pipeline",  # asset packaging library
        "south", # migrations
        'djcelery', # tasks scheduling
        'kombu.transport.django', # transport layer
        'adminplus',

    )
    # apps local for this project go here.
    LOCAL_APPS = (
        "config",
        "apps.pages",
        "apps.feeds",
        "feeds",
        "spiders",
    )
    INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS


class Assets(object):
    ########## SLUGLIFIER
    AUTOSLUG_SLUGIFY_FUNCTION = "slugify.slugify"
    ########## END SLUGLIFIER

    #### django-crispy-forms settings
    CRISPY_TEMPLATE_PACK = "bootstrap3"
    CRISPY_FAIL_SILENTLY = not Base.DEBUG
    #### end django-crispy-forms settings

    #### fixtures settings.
    FIXTURE_DIRS = (join(BASE_DIR, "fixtures"),)
    #### end fixtures settings.


    #### media settings.
    MEDIA_ROOT = join(BASE_DIR, "media")
    MEDIA_URL = "/media/"
    #### end Media settings.

    #### Package: django-pipeline settings.
    PIPELINE_COMPILERS = (
        "pipeline.compilers.coffee.CoffeeScriptCompiler",
        "pipeline.compilers.stylus.StylusCompiler",
    )
    PIPELINE_CSS = {
        "style": {
            "source_filenames": (
                "css/style.styl",
            ),
            "output_filename": "css/style.css",
            # "extra_context": {
            #     "media": "screen,projection",
            # },
        },

    }
    PIPELINE_JS = {
        "site": {
            "source_filenames": (
                "js/site.coffee",
            ),
            "output_filename": "js/site.js",
        },
    }
    PIPELINE_CSS_COMPRESSOR = "pipeline.compressors.yuglify.YuglifyCompressor"
    PIPELINE_JS_COMPRESSOR = "pipeline.compressors.yuglify.YuglifyCompressor"
    PIPELINE_COFFEE_SCRIPT_BINARY = "/usr/bin/env coffee"
    PIPELINE_STYLUS_BINARY = "/usr/bin/env stylus"
    PIPELINE_YUGLIFY_BINARY = "/usr/bin/env yuglify"
    #### End Package: django-pipeline settings.

    #### static files settings.
    STATIC_ROOT = join(os.path.dirname(BASE_DIR), "staticfiles")
    STATIC_URL = "/static/"
    STATICFILES_DIRS = (join(BASE_DIR, "static"),)
    STATICFILES_FINDERS = (
        "django.contrib.staticfiles.finders.FileSystemFinder",
        "django.contrib.staticfiles.finders.AppDirectoriesFinder",
    )
    STATICFILES_STORAGE = "pipeline.storage.PipelineCachedStorage"  # using django-pipeline
    #### end static files settings.

    #### templates settings.
    TEMPLATE_DIRS = (join(BASE_DIR, "templates"),)
    TEMPLATE_LOADERS = (
        ("pyjade.ext.django.Loader", ( "django.template.loaders.filesystem.Loader",  # using django default
                                        "django.template.loaders.app_directories.Loader",  # using django default

        )),
    )
    #### end templates settings


class Authentication(object):
    ACCOUNT_AUTHENTICATION_METHOD = "email"
    ACCOUNT_EMAIL_REQUIRED = True
    ACCOUNT_EMAIL_VERIFICATION = "mandatory"
    ADMINS = (("productfinder Ltd", "enquiries@productfinder.com"),)
    #AUTH_USER_MODEL = "users.User"
    AUTHENTICATION_BACKENDS = (
        "django.contrib.auth.backends.ModelBackend",
        "allauth.account.auth_backends.AuthenticationBackend",
    )
    LOGIN_REDIRECT_URL = "users:redirect"
    MANAGERS = ADMINS


class Caching(object):
    # See: https://docs.djangoproject.com/en/dev/ref/settings/#caches
    CACHES = {
        "default": {
            "BACKEND": "django.core.cache.backends.locmem.LocMemCache",
            "LOCATION": ""
        }
    }


class ContextProcessors(object):
    # See: https://docs.djangoproject.com/en/dev/ref/settings/#template-context-processors
    TEMPLATE_CONTEXT_PROCESSORS = (
        "django.contrib.auth.context_processors.auth",

        # django-allauth context processor
        "allauth.account.context_processors.account",
        "allauth.socialaccount.context_processors.socialaccount",

        "django.core.context_processors.debug",
        "django.core.context_processors.i18n",
        "django.core.context_processors.media",
        "django.core.context_processors.static",
        "django.core.context_processors.tz",
        "django.contrib.messages.context_processors.messages",
        "django.core.context_processors.request",

        # django-constance context processor
        "constance.context_processors.config",

        # custom context processor
        "config.context_processors.site",
    )


class Database(object):
    # See: https://docs.djangoproject.com/en/dev/ref/settings/#databases
    # See: https://pypi.python.org/pypi/dj-database-url/
    DATABASES = values.DatabaseURLValue("postgres://vagrant:vagrant@localhost:5432/base")


class Email(object):
    # See: https://docs.djangoproject.com/en/dev/ref/settings/#std:setting-EMAIL_BACKEND
    EMAIL_BACKEND = values.Value("django.core.mail.backends.smtp.EmailBackend")


class ElasticSearch(object):
    #### Elasticsearch settings.
    # See: http://nanvel.name/weblog/django-haystack-elasticsearch-example-project/#sthash.nz7skcpw.dpuf
    HAYSTACK_CONNECTIONS = {
        "default": {
            "ENGINE": "haystack.backends.elasticsearch_backend.ElasticsearchSearchEngine",
            "URL": "http://127.0.0.1:9200/",
            "INDEX_NAME": "haystack",
        },
    }
    HAYSTACK_SIGNAL_PROCESSOR = "haystack.signals.RealtimeSignalProcessor"
    #### End elasticsearch settings.


class Localization(object):
    # See: https://docs.djangoproject.com/en/dev/ref/settings
    LANGUAGE_CODE = "en-gb"
    TIME_ZONE = "Europe/London"
    USE_I18N = values.BooleanValue(True)
    USE_L10N = values.BooleanValue(True)
    USE_TZ = values.BooleanValue(True)


class Logging(object):
    # See: https://docs.djangoproject.com/en/dev/ref/settings/#logging
    LOGGING = {
        "version": 1,
        "disable_existing_loggers": False,
        "filters": {
            "require_debug_false": {
                "()": "django.utils.log.RequireDebugFalse"
            }
        },
        "handlers": {
            "mail_admins": {
                "level": "ERROR",
                "filters": ["require_debug_false"],
                "class": "django.utils.log.AdminEmailHandler"
            }
        },
        "loggers": {
            "django.request": {
                "handlers": ["mail_admins"],
                "level": "ERROR",
                "propagate": True,
            },
        }
    }


class MiddleWare(object):
    # See: https://docs.djangoproject.com/en/dev/ref/settings/#middleware-classes
    MIDDLEWARE_CLASSES = (
        "django.contrib.sessions.middleware.SessionMiddleware",
        "django.middleware.common.CommonMiddleware",
        "django.middleware.csrf.CsrfViewMiddleware",
        "django.contrib.auth.middleware.AuthenticationMiddleware",
        "django.contrib.messages.middleware.MessageMiddleware",
        "django.middleware.clickjacking.XFrameOptionsMiddleware",
        "django.middleware.gzip.GZipMiddleware",
        "pipeline.middleware.MinifyHTMLMiddleware",
    )



