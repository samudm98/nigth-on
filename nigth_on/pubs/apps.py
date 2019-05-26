from django.apps import AppConfig


class PubsAppConfig(AppConfig):

    name = "nigth_on.pubs"
    verbose_name = "Pubs"

    def ready(self):
        try:
            import pubs.signals  # noqa F401
        except ImportError:
            pass
