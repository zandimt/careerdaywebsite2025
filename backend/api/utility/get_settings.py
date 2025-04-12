from constance import config
from django.conf import settings


def get_settings():
    settings_list = {}
    for key, options in getattr(settings, "CONSTANCE_CONFIG", {}).items():
        settings_list[key] = getattr(config, key)

    return settings_list
