"""General view Mixins for NDH."""
from django.contrib.auth.mixins import UserPassesTestMixin
from django.views.generic.base import ContextMixin


class AttrContextMixin(ContextMixin):
    """Mixin to add view attributes to context."""

    attr_context = []

    def get_context_data(self, **kwargs):
        """Update context from attributes."""
        return super().get_context_data(
            **{key: getattr(self, key) for key in self.attr_context},
            **kwargs,
        )


class SuperUserRequiredMixin(UserPassesTestMixin):
    """Mixin that allow access only to superusers."""

    def test_func(self):
        """Check that the user has superuser access."""
        return self.request.user.is_superuser


class NDHFormMixin(AttrContextMixin):
    """Mixin setting a default form template and title."""

    template_name = "ndh/base_form.html"
    title = ""
    continue_edit = False
    attr_context = ["title", "continue_edit"]

    def get_success_url(self):
        """Redirect to current page if continue_edit."""
        if self.continue_edit and "continue_edit" in self.request.GET:
            return self.request.path
        return super().get_success_url()


class NDHDeleteMixin(NDHFormMixin):
    """Mixin setting a default template for delete views."""

    template_name = "ndh/base_delete.html"
