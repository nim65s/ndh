from django.forms import ModelForm

from .models import TestModel

from ndh.forms import AccessibleDateTimeField


class TestForm(ModelForm):
    moment = AccessibleDateTimeField()

    class Meta:
        model = TestModel
        fields = ('name', 'year_in_school', 'tests', 'moment')
