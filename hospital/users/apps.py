from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class UsersConfig(AppConfig):
    name = "hospital.users"
    verbose_name = _("Manager Users")

    def ready(self):
        try:
            import hospital.users.signals  # noqa F401
        except ImportError:
            pass
