from django.apps import AppConfig


class ProductsAppConfig(AppConfig):

    name = "nigth_on.products"
    verbose_name = "Products"

    def ready(self):
        try:
            import products.signals  # noqa F401
        except ImportError:
            pass
