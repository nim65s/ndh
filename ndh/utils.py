from django.contrib.sites.models import Site


def full_url(url=''):
    return 'https://' + Site.objects.get_current().domain + url
