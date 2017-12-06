from datetime import timedelta

from django.test import TestCase
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User

from ndh.utils import query_sum

from .models import TestModel


class TestNDH(TestCase):
    def test_models(self):

        # test creation
        self.assertEqual(TestModel.objects.count(), 0)
        TestModel.objects.create(name='Pipo 22 é@ü', moment=timezone.now())
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
        self.assertEqual(instance.get_admin_url(), '/admin/testproject/testmodel/1/change/')

        # test query_sum
        self.assertEqual(query_sum(TestModel.objects.all(), 'tests'), 42)

        # test enum_to_choices
        self.assertEqual(instance.get_year_in_school_display(), 'freshman')

    def test_templatetags(self):
        r = self.client.get(reverse('test'))
        self.assertEqual(r.status_code, 200)
        mail = '<span class="mail">test<span class="at"></span>example<span class="dot"></span>org</span>'
        self.assertIn(mail, r.content.decode())

        User.objects.create_user(username='test', password='test')
        self.client.login(username='test', password='test')

        r = self.client.get(reverse('test'))
        self.assertEqual(r.status_code, 200)
        mail = '<span class="mail"><a href="mailto:test@example.org">test@example.org</a></span>'
        self.assertIn(mail, r.content.decode())

    def test_views(self):
        self.assertEqual(TestModel.objects.count(), 0)
        r = self.client.get(reverse('create'))
        self.assertEqual(r.status_code, 200)
        data = {'name': 'Pipè', 'year_in_school': 2, 'tests': 3, 'moment_0': '2017-12-06', 'moment_1': '03:19:45'}
        r = self.client.post(reverse('create'), data)

        self.assertEqual(TestModel.objects.count(), 1)

        r = self.client.get(reverse('delete', args=[TestModel.objects.first().pk]))
        self.assertEqual(r.status_code, 200)

        self.assertEqual(TestModel.objects.count(), 1)

        r = self.client.post(reverse('delete', args=[TestModel.objects.first().pk]))
        self.assertEqual(r.status_code, 302)

        self.assertEqual(TestModel.objects.count(), 0)
