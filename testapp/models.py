"""Models for the testapp."""

from django.db import models

from ndh.models import Links, NamedModel, TimeStampedModel


class TestModel(Links, TimeStampedModel, NamedModel):
    """Main test model."""

    tests = models.IntegerField(default=42)
    tests_decimal = models.DecimalField(default=3.14, max_digits=5, decimal_places=2)
    moment = models.DateTimeField()
    datalist = models.CharField(max_length=30)


class TestModelList(TestModel):
    """Test model for get_absolute_url for lists."""

    absolute_url_detail = False


class TestModelPK(Links, TimeStampedModel):
    """Test model for get_absolute_url for objects."""

    pass
