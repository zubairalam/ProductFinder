from configurations import Configuration
from . import *


class Common(Apps, Assets, Authentication, Base, Caching, ContextProcessors, Database, Email, ElasticSearch,
             Localization, Logging, MiddleWare):
    """
    The common settings and the default configuration.
    """
    pass


class Local(Common, Configuration):
    """
    The in-development settings and default configuration.
    """
    #### email settings
    EMAIL_HOST = "localhost"
    EMAIL_PORT = 1025
    EMAIL_BACKEND = values.Value('django.core.mail.backends.console.EmailBackend')
    #### end email settings

    #### installed apps overwrite.
    INSTALLED_APPS = Common.INSTALLED_APPS
    INSTALLED_APPS += ('debug_toolbar', 'haystack_panel')
    #### end installed apps overwrite.

    #### django-debug-toolbar settings.
    MIDDLEWARE_CLASSES = Common.MIDDLEWARE_CLASSES + ('debug_toolbar.middleware.DebugToolbarMiddleware',)
    DEBUG_TOOLBAR_CONFIG = {
        'INTERCEPT_REDIRECTS': False,
    }
    DEBUG_TOOLBAR_PANELS = (
        'debug_toolbar.panels.versions.VersionsPanel',
        'debug_toolbar.panels.timer.TimerPanel',
        'debug_toolbar.panels.settings.SettingsPanel',
        'debug_toolbar.panels.headers.HeadersPanel',
        'debug_toolbar.panels.request.RequestPanel',
        'debug_toolbar.panels.sql.SQLPanel',
        'debug_toolbar.panels.staticfiles.StaticFilesPanel',
        'debug_toolbar.panels.templates.TemplatesPanel',
        'debug_toolbar.panels.cache.CachePanel',
        'debug_toolbar.panels.signals.SignalsPanel',
        'debug_toolbar.panels.logging.LoggingPanel',
        'debug_toolbar.panels.redirects.RedirectsPanel',
        'haystack_panel.panel.HaystackDebugPanel',
    )

    INTERNAL_IPS = ('127.0.0.1',
                    '10.0.2.2',  # Useful if using vagrant request.META['REMOTE_ADDR']
    )
    #### end django-debug-toolbar settings.


class Staging(Common, Configuration):
    pass
    # DEBUG = False
    # TEMPLATE_DEBUG = DEBUG
    # SECRET_KEY = values.SecretValue()


class Production(Common, Configuration):
    """
    The production settings and default configuration.
    """
    pass
    # DEBUG = False
    # TEMPLATE_DEBUG = DEBUG
    # SECRET_KEY = values.SecretValue()
