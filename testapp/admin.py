"""Admin configuration for the test app."""

from django.contrib.admin import site

from .models import TestModel, TestModelList, TestModelPK

site.register(TestModel)
site.register(TestModelList)
site.register(TestModelPK)
