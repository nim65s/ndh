"""General utils for NDH."""
import os
from typing import Generator, Optional, Tuple, TypeVar
from warnings import warn

from django.db import models
from django.db.models.functions import Coalesce

Numeric = TypeVar('Numeric', int, float)


def full_url(url: str = '', domain: str = None, protocol: str = 'https') -> str:
    """Prepend protocol (default to https) and domain name (default from the Site framework) to an url."""
    if domain is None:
        from django.contrib.sites.models import Site
        domain = Site.objects.get_current().domain
    return f'{protocol}://{domain}{url}'


def enum_to_choices(enum) -> Generator[Tuple[int, str], None, None]:
    """Allow to use an Enum as choices in a model field."""
    url = "https://docs.djangoproject.com/en/3.0/ref/models/fields/#enumeration-types"
    warn(f"ndh.utils.enum_to_choices is deprecated. Please switch to {url}", DeprecationWarning)
    return ((item.value, item.name) for item in list(enum))


def query_sum(queryset: models.QuerySet, field: str, output_field: Optional[models.Field] = None) -> Numeric:
    """Let the DBMS perform a sum on a queryset."""
    return queryset.aggregate(s=Coalesce(models.Sum(field), 0, output_field=output_field))['s']


def get_env(env_file: str = '.env') -> None:
    """Set default environment variables from .env file."""
    try:
        with open(env_file) as f_h:
            for line in f_h.readlines():
                try:
                    key, val = line.split('=', maxsplit=1)
                    os.environ.setdefault(key.strip(), val.strip())
                except ValueError:
                    pass
    except FileNotFoundError:
        pass
