"""Models for the testapp."""
from enum import IntEnum

from django.db import models

from ndh.models import Links, NamedModel, TimeStampedModel
from ndh.utils import enum_to_choices


class TestModel(Links, TimeStampedModel, NamedModel):
    """Main test model."""
    YEARS_IN_SCHOOL = IntEnum('years_in_school', 'freshman sophomore junior senior')

    year_in_school = models.IntegerField(choices=enum_to_choices(YEARS_IN_SCHOOL), default=1)
    tests = models.IntegerField(default=42)
    moment = models.DateTimeField()


class TestModelList(TestModel):
    """Test model for get__absolute_url for lists."""
    absolute_url_detail = False


class TestModelPK(Links, TimeStampedModel):
    """Test model for get_absolute_url for objects."""
    pass
