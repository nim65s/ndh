"""General context processors for NDH."""
from typing import Dict

from django.conf import settings
from django.http import HttpRequest


def settings_constants(request: HttpRequest) -> Dict[str, str]:
    """Set constants from settings to template contexts."""
    ret = {}
    if hasattr(settings, "NDH_TEMPLATES_SETTINGS"):
        ret = {key: getattr(settings, key) for key in settings.NDH_TEMPLATES_SETTINGS}
    return ret
