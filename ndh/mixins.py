"""General view Mixins for NDH."""
from django.contrib.auth.mixins import UserPassesTestMixin


class SuperUserRequiredMixin(UserPassesTestMixin):
    """Mixin that allow access only to superusers."""
    def test_func(self):
        """Check that the user has superuser access."""
        return self.request.user.is_superuser


class NDHFormMixin(object):
    """Mixin setting a default form template and title."""
    template_name = 'ndh/base_form.html'
    title = ''

    def get_context_data(self, **kwargs):
        """Add title to the context."""
        return super().get_context_data(title=self.title, **kwargs)


class NDHDeleteMixin(NDHFormMixin):
    """Mixin setting a default template for delete views."""
    template_name = 'ndh/base_delete.html'
