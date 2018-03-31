from django.conf import settings


def settings_constants(request):
    if hasattr(settings, 'NDH_TEMPLATES_SETTINGS'):
        return {key: getattr(settings, key) for key in settings.NDH_TEMPLATES_SETTINGS}
    return {}
