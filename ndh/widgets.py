"""NDH Widgets."""

from django.forms.widgets import DateInput, TextInput

DATE_FORMAT = "%Y-%m-%d"
TYPE_DATE = {"type": "date"}
TYPE_TIME = {"type": "time"}


class AccessibleDateInput(DateInput):
    """Set date HTML type."""

    def __init__(self):
        """Initialize with date type."""
        super().__init__(attrs=TYPE_DATE, format=DATE_FORMAT)


class DatalistInput(TextInput):
    """Datalist widget."""

    template_name = "ndh/forms/widgets/datalist.html"

    def __init__(self, datalist=None, **attrs):
        """Initialize with datalist."""
        self.datalist = datalist
        super().__init__(**attrs)

    def get_context(self, name, value, attrs):
        """Add datalist to the context."""
        context = super().get_context(name, value, attrs)
        context["datalist"] = (
            self.datalist() if callable(self.datalist) else self.datalist
        )
        return context
