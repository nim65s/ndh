"""Helpers for models."""
from typing import Any

from django.db import models
from django.urls import reverse
from django.utils.safestring import mark_safe
from django.utils.translation import gettext_lazy as _

from autoslug import AutoSlugField  # type: ignore

from .querysets import NameOrderedQuerySet
from .utils import full_url


class Links:
    """A mixin to get links."""

    id: int  # noqa: A003
    pk: int
    slug: str
    _meta: Any
    absolute_url_detail: bool = True
    create_view_name_suffix = "-add"
    delete_view_name_suffix = "-delete"
    detail_view_name_suffix = ""
    list_view_name_suffix = "s"
    update_view_name_suffix = "-update"

    def get_pk_or_slug(self):
        """Provide the right kwargs for reverse()."""
        return {"slug": self.slug} if hasattr(self, "slug") else {"pk": self.pk}

    @classmethod
    def get_view_name(cls, suffix, app=True) -> str:
        """Provide the common view name prefix."""
        app = f"{cls._meta.app_label}:" if app else ""
        return f"{app}{cls._meta.model_name}{suffix}"

    @classmethod
    def get_create_url(cls, app=True) -> str:
        """Get the absolute url to create an instance of this model."""
        return reverse(cls.get_view_name(cls.create_view_name_suffix, app))

    def get_delete_url(self, app=True) -> str:
        """Get the absolute url to delete an instance of this model."""
        return reverse(
            self.get_view_name(self.delete_view_name_suffix, app),
            kwargs=self.get_pk_or_slug(),
        )

    def get_detail_url(self, app=True) -> str:
        """Get the absolute url to detail an instance of this model."""
        return reverse(
            self.get_view_name(self.detail_view_name_suffix, app),
            kwargs=self.get_pk_or_slug(),
        )

    @classmethod
    def get_list_url(cls, app=True) -> str:
        """Get the absolute url to list instances of this model."""
        return reverse(cls.get_view_name(cls.list_view_name_suffix, app))

    def get_update_url(self, app=True) -> str:
        """Get the absolute url to update an instance of this model."""
        return reverse(
            self.get_view_name(self.update_view_name_suffix, app),
            kwargs=self.get_pk_or_slug(),
        )

    def get_absolute_url(self) -> str:
        """Get the absolute url for a queryset or an instance."""
        if self.absolute_url_detail:
            return self.get_detail_url()
        return self.get_list_url()

    def get_admin_url(self) -> str:
        """Get the admin url for an instance."""
        return reverse(
            f"admin:{self._meta.app_label}_{self._meta.model_name}_change",
            args=[self.id],
        )

    def get_full_admin_url(self) -> str:
        """Get the protocol + domain + admin_url."""
        return full_url(self.get_admin_url())

    def get_full_url(self) -> str:
        """Get the protocol + domain + absolute_url."""
        return full_url(self.get_absolute_url())

    def get_link(self) -> str:
        """Get the HTML link for this absolute_url."""
        return mark_safe(f'<a href="{self.get_absolute_url()}">{self}</a>')

    def get_md_link(self) -> str:
        """Get the Markdown link for this absolute_url."""
        return mark_safe(f"[{self}]({self.get_absolute_url()})")

    def get_full_link(self) -> str:
        """Get the full HTML link for this absolute_url."""
        return mark_safe(f'<a href="{self.get_full_url()}">{self}</a>')

    def get_full_md_link(self) -> str:
        """Get the full Markdown link for this absolute_url."""
        return mark_safe(f"[{self}]({self.get_full_url()})")


class TimeStampedModel(models.Model):
    """Mixin to timestamp a model."""

    created = models.DateTimeField(auto_now_add=True, verbose_name=_("created"))
    updated = models.DateTimeField(auto_now=True, verbose_name=_("updated"))

    class Meta:
        """Meta."""

        abstract = True


class NamedModel(models.Model):
    """Mixin to name and slugify a model."""

    name = models.CharField(max_length=200, unique=True, verbose_name=_("name"))
    slug = AutoSlugField(populate_from="name", unique=True)

    objects = NameOrderedQuerySet.as_manager()

    class Meta:
        """Meta."""

        abstract = True

    def __str__(self) -> str:
        """Get the name of the instance."""
        return self.name
