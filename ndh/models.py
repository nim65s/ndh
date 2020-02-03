"""Helpers for models."""
from typing import Any

from django.db import models
from django.urls import reverse
from django.utils.safestring import mark_safe

from autoslug import AutoSlugField  # type: ignore

from .querysets import NameOrderedQuerySet
from .utils import full_url


class Links:
    """A mixin to get links."""
    id: int
    pk: int
    slug: str
    _meta: Any
    absolute_url_detail: bool = True

    def get_absolute_url(self) -> str:
        """Get the absolute url for a queryset or an instance."""
        app, model = self._meta.app_label, self._meta.model_name
        if self.absolute_url_detail:
            return reverse(f'{app}:{model}', kwargs={'slug': self.slug} if hasattr(self, 'slug') else {'pk': self.pk})
        else:
            return reverse(f'{app}:{model}s')

    def get_full_url(self) -> str:
        """Get the protocol + domain + absolute_url."""
        return full_url(self.get_absolute_url())

    def get_admin_url(self) -> str:
        """Get the admin url for an instance."""
        return reverse(f'admin:{self._meta.app_label}_{self._meta.model_name}_change', args=[self.id])

    def get_link(self) -> str:
        """Get the HTML link for this absolute_url."""
        return mark_safe(f'<a href="{self.get_absolute_url()}">{self}</a>')


class TimeStampedModel(models.Model):
    """Mixin to timestamp a model."""
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        """Meta."""
        abstract = True


class NamedModel(models.Model):
    """Mixin to name and slugify a model."""
    name = models.CharField(max_length=200, unique=True)
    slug = AutoSlugField(populate_from='name', unique=True)

    objects = NameOrderedQuerySet.as_manager()

    class Meta:
        """Meta."""
        abstract = True

    def __str__(self) -> str:
        """Get the name of the instance."""
        return self.name
