"""NDH Widgets."""
from django.forms.widgets import TextInput


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
