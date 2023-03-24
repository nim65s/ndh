"""General context processors for NDH."""

from django.conf import settings
from django.http import HttpRequest


def settings_constants(request: HttpRequest) -> dict[str, str]:
    """Set constants from settings to template contexts."""
    if hasattr(settings, "NDH_TEMPLATES_SETTINGS"):
        return {key: getattr(settings, key) for key in settings.NDH_TEMPLATES_SETTINGS}
    return {}
