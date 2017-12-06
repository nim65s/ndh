from django.views.generic import CreateView, DeleteView

from .forms import TestForm
from .models import TestModel


class TestCreateView(CreateView):
    model = TestModel
    form_class = TestForm


class TestDeleteView(DeleteView):
    model = TestModel
    success_url = 'create'
