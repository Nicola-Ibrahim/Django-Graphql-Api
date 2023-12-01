"""Third-party package configuration settings"""


from datetime import timedelta

from config.settings.utils.misc import get_singing_key

INSTALLED_APPS += (  # type: ignore # noqa: F821
    "corsheaders",
    "graphene_django",
)


GRAPHENE = {
    "SCHEMA": "django_root.schema.schema",
}
