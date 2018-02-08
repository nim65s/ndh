from django.db import models
from django.urls import reverse
from django.utils.safestring import mark_safe

from autoslug import AutoSlugField

from .utils import full_url


class Links(object):
    absolute_url_detail = True

    def get_absolute_url(self):
        app, model = self._meta.app_label, self._meta.model_name
        if self.absolute_url_detail:
            return reverse(f'{app}:{model}', kwargs={'slug': self.slug})
        else:
            return reverse(f'{app}:{model}s')

    def get_full_url(self):
        return full_url(self.get_absolute_url())

    def get_admin_url(self):
        return reverse(f'admin:{self._meta.app_label}_{self._meta.model_name}_change', args=[self.id])

    def get_link(self):
        return mark_safe(f'<a href="{self.get_absolute_url()}">{self}</a>')


class TimeStampedModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class NamedModel(models.Model):
    name = models.CharField(max_length=200, unique=True)
    slug = AutoSlugField(populate_from='name', unique=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name
