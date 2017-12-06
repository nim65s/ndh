from django import forms


class AccessibleDateTimeField(forms.SplitDateTimeField):
    widget = forms.SplitDateTimeWidget(
        date_attrs={'type': 'date'},
        time_attrs={'type': 'time'})
