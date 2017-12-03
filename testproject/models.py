from django.db import models

from ndh.models import Links, NamedModel, TimeStampedModel


class TestModel(Links, TimeStampedModel, NamedModel):
    tests = models.IntegerField(default=42)

    def get_absolute_url(self):
        return f'/test/{self.slug}'
