"""General Form-related helpers for NDH."""

from django import forms

from .widgets import DATE_FORMAT, TYPE_DATE, TYPE_TIME, DatalistInput


class AccessibleDateTimeField(forms.SplitDateTimeField):
    """Set date & time HTML types."""

    widget = forms.SplitDateTimeWidget(
        date_format=DATE_FORMAT,
        date_attrs=TYPE_DATE,
        time_attrs=TYPE_TIME,
    )  # type: ignore


class DatalistField(forms.CharField):
    """A CharField with datalist options."""

    def __init__(self, datalist=None, **kwargs):
        """Initialize with datalist."""
        super().__init__(widget=DatalistInput(datalist), **kwargs)
