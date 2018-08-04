from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView

from ndh.mixins import NDHDeleteMixin, NDHFormMixin, SuperUserRequiredMixin

from .forms import TestForm
from .models import TestModel


class TestCreateView(NDHFormMixin, CreateView):
    model = TestModel
    form_class = TestForm
    title = 'Create Test'


class TestDeleteView(NDHDeleteMixin, SuperUserRequiredMixin, DeleteView):
    model = TestModel
    success_url = reverse_lazy('testapp:testmodels')
    title = 'Delete Test'
