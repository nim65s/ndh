"""Forms for the testapp."""
from django.forms import ModelForm

from ndh.forms import AccessibleDateTimeField

from .models import TestModel


class TestForm(ModelForm):
    """Form to test ndh.forms."""

    moment = AccessibleDateTimeField()

    class Meta:
        """ModelForm definitions."""

        model = TestModel
        fields = ('name', 'tests', 'moment')
