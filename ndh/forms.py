"""General Form-related helpers for NDH."""
from django import forms

from .widgets import DatalistInput


class AccessibleDateTimeField(forms.SplitDateTimeField):
    """Set date & time HTML types."""

    widget = forms.SplitDateTimeWidget(
        date_format="%Y-%m-%d",
        date_attrs={"type": "date"},
        time_attrs={"type": "time"},
    )  # type: ignore


class DatalistField(forms.CharField):
    """A CharField with datalist options."""

    def __init__(self, datalist=None, **kwargs):
        """Initialize with datalist."""
        super().__init__(widget=DatalistInput(datalist), **kwargs)
