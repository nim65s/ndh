from django.db.models import QuerySet


class NameOrderedQuerySet(QuerySet):
    def name_ordered(self) -> QuerySet:
        return self.order_by('name')
