"""General QuerySets for NDH."""
from django.db.models import QuerySet


class NameOrderedQuerySet(QuerySet):
    """Order a queryset on the "name" field."""
    def name_ordered(self) -> QuerySet:
        """Order by name."""
        return self.order_by('name')
