from django.contrib.sites.models import Site
from django.db import models


def full_url(url=''):
    return 'https://' + Site.objects.get_current().domain + url


def enum_to_choices(enum):
    return ((item.value, item.name) for item in list(enum))


def query_sum(queryset, field):
    return queryset.aggregate(s=models.functions.Coalesce(models.Sum(field), 0))['s']
