"""Admin configuration for the test app."""
from django.contrib.admin import site

from .models import TestModel

site.register(TestModel)
