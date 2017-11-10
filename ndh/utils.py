from django.contrib.sites.models import Site


def full_url(url=''):
    return 'https://' + Site.objects.get_current().domain + url


def enum_to_choices(enum):
        return ((item.value, item.name) for item in list(enum))
