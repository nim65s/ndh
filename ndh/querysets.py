from django.db import models


class NameOrderedQuerySet(models.QuerySet):
    def name_ordered(self):
        return self.order_by('name')
