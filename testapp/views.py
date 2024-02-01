"""Views for testapp."""

from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, UpdateView

from ndh.mixins import NDHDeleteMixin, NDHFormMixin, SuperUserRequiredMixin

from .forms import TestForm
from .models import TestModel


class TestCreateView(NDHFormMixin, CreateView):
    """View to test NDHFormMixin."""

    model = TestModel
    form_class = TestForm
    title = "Create Test"


class TestUpdateView(NDHFormMixin, UpdateView):
    """View to test NDHFormMixin continue_edit."""

    model = TestModel
    form_class = TestForm
    title = "Update Test"
    continue_edit = True


class TestDeleteView(NDHDeleteMixin, SuperUserRequiredMixin, DeleteView):
    """View to test other mixins."""

    model = TestModel
    success_url = reverse_lazy("testapp:testmodels")
    title = "Delete Test"
