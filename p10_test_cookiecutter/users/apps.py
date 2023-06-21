from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class UsersConfig(AppConfig):
    name = "p10_test_cookiecutter.users"
    verbose_name = _("Users")

    def ready(self):
        try:
            import p10_test_cookiecutter.users.signals  # noqa: F401
        except ImportError:
            pass
