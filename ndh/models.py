from django.core.urlresolvers import reverse
from django.utils.safestring import mark_safe

from .utils import full_url


class Links(object):
    def get_full_url(self):
        return full_url(self.get_absolute_url())

    def get_admin_url(self):
        return reverse(f'admin:{self._meta.app_label}_{self._meta.model_name}_change', args=self.id)

    def get_link(self):
        return mark_safe(f'<a href="{self.get_absolute_url}">{self}</a>')
