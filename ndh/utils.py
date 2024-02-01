"""General utils for NDH."""

import os
from pathlib import Path
from typing import TYPE_CHECKING, TypeVar, Union

from django.db import models
from django.db.models.functions import Coalesce

if TYPE_CHECKING:  # pragma: no cover
    from django.db.models.manager import RelatedManager

Numeric = TypeVar("Numeric", int, float)


def full_url(url: str = "", domain: None | str = None, protocol: str = "https") -> str:
    """Prepend protocol and domain name to an url."""
    if domain is None:
        from django.contrib.sites.models import Site

        domain = Site.objects.get_current().domain
    return f"{protocol}://{domain}{url}"


def query_sum(
    queryset: Union[models.QuerySet, "RelatedManager"],
    field: str,
    output_field: models.Field | None = None,
) -> Numeric:
    """Let the DBMS perform a sum on a queryset."""
    return queryset.aggregate(
        s=Coalesce(models.Sum(field), 0, output_field=output_field),
    )["s"]


def get_env(env_file: str = ".env") -> None:
    """Set default environment variables from .env file."""

    def load_env(path: Path):
        with path.open() as f:
            for line in f.readlines():
                if line.startswith("#"):
                    continue
                try:
                    key, val = line.split("=", maxsplit=1)
                    os.environ.setdefault(key.strip(), val.strip())
                except ValueError:
                    pass

    current = Path(env_file)
    parent = Path().parent / env_file
    if current.exists():
        load_env(current)
    elif parent.exists():
        load_env(parent)


def set_env(var: str, val: str, env_file: str = ".env") -> None:
    """Set default environment variables from .env file."""

    def update_env(path: Path):
        with path.open() as f:
            lines = f.readlines()

        updated = False

        with path.open("w") as f:
            for line in lines:
                if not line.startswith("#") and line.split("=")[0].strip() == var:
                    print(f"{var} = {val}", file=f)
                    updated = True
                else:
                    print(line.strip(), file=f)
            if not updated:
                print(f"{var} = {val}", file=f)

    current = Path(env_file)
    parent = Path().parent / env_file
    if current.exists():
        update_env(current)
    elif parent.exists():
        update_env(parent)
