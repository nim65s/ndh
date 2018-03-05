import os

from django.db import models


def full_url(url='', domain=None, protocol='https'):
    """
    Prepend protocol (default to https) and domain name (default from the Site framework) to an url
    """
    if domain is None:
        from django.contrib.sites.models import Site
        domain = Site.objects.get_current().domain
    return f'{protocol}://{domain}{url}'


def enum_to_choices(enum):
    return ((item.value, item.name) for item in list(enum))


def query_sum(queryset, field):
    """
    Let the DBMS perform a sum on a queryset
    """
    return queryset.aggregate(s=models.functions.Coalesce(models.Sum(field), 0))['s']


def get_env(env_file='.env'):
    """
    Set default environment variables from .env file
    """
    try:
        with open(env_file) as f:
            for line in f.readlines():
                try:
                    key, val = line.split('=')
                    os.environ.setdefault(key.strip(), val.strip())
                except ValueError:
                    pass
    except FileNotFoundError:
        pass
