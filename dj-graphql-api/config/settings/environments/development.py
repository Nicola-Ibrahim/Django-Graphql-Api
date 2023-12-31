from corsheaders.defaults import default_headers

DEBUG = True
SECRET_KEY = "jd@11j#vr_+36p&f)nm9_9ocpt^o!^*fgd(nyhrx1r#xf9_p&5"

# ref: https://stackoverflow.com/questions/34360912/deploying-django-app-with-docker-allowed-hosts
# The domain should be added to ALLOWED_HOSTS to be accessible

INSTALLED_APPS += (  # type: ignore # noqa: F821
    "debug_toolbar",
    "django_extensions",
)

ALLOWED_HOSTS = ["127.0.0.1", "localhost"]

# Logger configurations
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "standard": {"format": "%(asctime)s %(levelname)s %(name)s %(message)s"},
        "colored": {
            "()": "colorlog.ColoredFormatter",
            "format": "%(log_color)s%(asctime)s %(levelname)s %(name)s %(bold_white)s%(message)s",
        },
    },
    "handlers": {
        "console": {
            "level": "INFO",
            "class": "colorlog.StreamHandler",
            "formatter": "colored",
            "filters": [],
        },
        # "file": {
        #     "level": "DEBUG",
        #     "class": "logging.FileHandler",
        #     "filename": "/logging/django.log",
        #     "formatter": "colored",
        # },
    },
    "loggers": {
        logger_name: {
            "handlers": ["console"],
            "level": "WARNING",
            "propagate": True,
        }
        for logger_name in (
            "django",
            "django.request",
            "django.db.backends",
            "django.template",
            "core",
            "urllib3",
            "asyncio",
        )
    },
    "root": {
        "level": "DEBUG",
        "handlers": ["console"],
    },
}


# Model graph configurations
GRAPH_MODELS = {
    "all_applications": True,
    "group_models": True,
}

# Debugger configurations
MIDDLEWARE += ("debug_toolbar.middleware.DebugToolbarMiddleware",)
INTERNAL_IPS = [
    "127.0.0.1",
]

DEBUG_TOOLBAR_PANELS = [
    "debug_toolbar.panels.history.HistoryPanel",
    "debug_toolbar.panels.versions.VersionsPanel",
    "debug_toolbar.panels.timer.TimerPanel",
    "debug_toolbar.panels.settings.SettingsPanel",
    "debug_toolbar.panels.headers.HeadersPanel",
    "debug_toolbar.panels.request.RequestPanel",
    "debug_toolbar.panels.sql.SQLPanel",
    "debug_toolbar.panels.staticfiles.StaticFilesPanel",
    "debug_toolbar.panels.templates.TemplatesPanel",
    "debug_toolbar.panels.cache.CachePanel",
    "debug_toolbar.panels.signals.SignalsPanel",
    "debug_toolbar.panels.redirects.RedirectsPanel",
    "debug_toolbar.panels.profiling.ProfilingPanel",
]


CORS_ALLOW_HEADERS = (*default_headers,)

CORS_ALLOWED_ORIGINS = [
    "http://localhost:8080",
    "http://127.0.0.1:8080",
]

CSRF_TRUSTED_ORIGINS = [
    "http://127.0.0.1:8080",
]
