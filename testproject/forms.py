from django.forms import ModelForm

from ndh.forms import AccessibleDateTimeField

from .models import TestModel


class TestForm(ModelForm):
    moment = AccessibleDateTimeField()

    class Meta:
        model = TestModel
        fields = ('name', 'year_in_school', 'tests', 'moment')
