"""Forms for the testapp."""

from django.forms import ModelForm

from ndh.forms import AccessibleDateTimeField, DatalistField

from .models import TestModel


def get_datalist():
    """Generate some datalist."""
    return {c * 8: f"Many {c}" for c in "auienrst"}


class TestForm(ModelForm):
    """Form to test ndh.forms."""

    moment = AccessibleDateTimeField()
    datalist = DatalistField(datalist=get_datalist)

    class Meta:
        """ModelForm definitions."""

        model = TestModel
        fields = ("name", "tests", "moment", "datalist")
