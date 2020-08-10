"""General Form-related helpers for NDH."""
from django import forms


class AccessibleDateTimeField(forms.SplitDateTimeField):
    """Set date & time HTML types."""
    widget = forms.SplitDateTimeWidget(date_attrs={'type': 'date'}, time_attrs={'type': 'time'})  # type: ignore
