from django.views.generic import CreateView, DeleteView

from ndh.mixins import NDHFormMixin, SuperUserRequiredMixin

from .forms import TestForm
from .models import TestModel


class TestCreateView(NDHFormMixin, CreateView):
    model = TestModel
    form_class = TestForm
    title = 'Create Test'


class TestDeleteView(NDHFormMixin, SuperUserRequiredMixin, DeleteView):
    model = TestModel
    success_url = 'create'
    title = 'Delete Test'
