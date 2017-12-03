from datetime import timedelta

from django.test import TestCase
from django.utils import timezone

from .models import TestModel


class TestNDH(TestCase):
    def test_models(self):

        # test creation
        self.assertEqual(TestModel.objects.count(), 0)
        TestModel.objects.create(name='Pipo 22 é@ü')
        self.assertEqual(TestModel.objects.count(), 1)

        # test name & slug
        instance = TestModel.objects.first()
        self.assertEqual(instance.name, str(instance))
        self.assertEqual(instance.slug, 'pipo-22-eu')

        # test datetimes
        self.assertLess(timezone.now() - instance.created, timedelta(seconds=5))
        almost_zero = instance.updated - instance.created
        self.assertLess(timedelta(0), almost_zero)
        self.assertLess(almost_zero, timedelta(seconds=1))
        instance.save()
        self.assertLess(almost_zero, instance.updated - instance.created)

        # test links
        self.assertEqual(instance.get_absolute_url(), f'/test/{instance.slug}')
        self.assertEqual(str(instance.get_link()), f'<a href="/test/{instance.slug}">{instance}</a>')
        self.assertEqual(instance.get_full_url(), f'https://example.com/test/{instance.slug}')
