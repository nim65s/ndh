from datetime import timedelta
import os

from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from ndh.utils import query_sum, get_env

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

        User.objects.create_user(username='super', password='super', is_superuser=True)
        self.client.login(username='super', password='super')

        TestModel.objects.create(name='Pipo 22 é@ü', moment=timezone.now())

        r = self.client.get(reverse('list'))
        self.assertIn('/admin/testproject/testmodel/', r.content.decode())

        r = self.client.get(TestModel.objects.first().get_absolute_url())
        self.assertIn('/admin/testproject/testmodel/1/change', r.content.decode())

    def test_views(self):
        self.assertEqual(TestModel.objects.count(), 0)
        r = self.client.get(reverse('create'))
        self.assertEqual(r.status_code, 200)
        data = {'name': 'Pipè', 'year_in_school': 2, 'tests': 3, 'moment_0': '2017-12-06', 'moment_1': '03:19:45'}
        r = self.client.post(reverse('create'), data)

        self.assertEqual(TestModel.objects.count(), 1)

        r = self.client.get(reverse('delete', args=[TestModel.objects.first().slug]))
        self.assertEqual(r.status_code, 302)

        User.objects.create_user(username='super', password='super', is_superuser=True)
        self.client.login(username='super', password='super')

        r = self.client.get(reverse('delete', args=[TestModel.objects.first().slug]))
        self.assertEqual(r.status_code, 200)

        self.assertEqual(TestModel.objects.count(), 1)

        r = self.client.post(reverse('delete', args=[TestModel.objects.first().slug]))
        self.assertEqual(r.status_code, 302)

        self.assertEqual(TestModel.objects.count(), 0)

    def test_utils(self):
        key, val, no_key, env_file = 'DJANGO_TEST_GET_ENV', 'it=works', 'KEY_WITHOUT_VAL', '.env'
        get_env(env_file)
        if key in os.environ:
            val = os.environ[key]
        else:
            with open(env_file, 'a') as f:
                print(f'{key}={val}', file=f)
        with open(env_file, 'a') as f:
            print(no_key, file=f)
        get_env(env_file)
        self.assertIn(key, os.environ)
        self.assertEqual(os.environ[key], val)
        self.assertNotIn(no_key, os.environ)

        # Clean the file
        with open(env_file) as f:
            lines = f.readlines()
        with open(env_file, 'w') as f:
            f.write('\n'.join(line for line in lines if not line.startswith(key) and not line.startswith(no_key)))
