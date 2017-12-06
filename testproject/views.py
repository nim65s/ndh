from django.views.generic import CreateView, DeleteView

from .models import TestModel
from .forms import TestForm


class TestCreateView(CreateView):
    model = TestModel
    form_class = TestForm


class TestDeleteView(DeleteView):
    model = TestModel
    success_url = 'create'
