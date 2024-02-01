"""Main entrypoint for test project & app."""

import os
from datetime import timedelta
from decimal import Decimal
from pathlib import Path

from django.contrib.auth.models import User
from django.db import models
from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from ndh.tests import TestNDHLinks
from ndh.utils import get_env, query_sum

from .models import TestModel, TestModelList, TestModelPK


class TestLinks(TestNDHLinks, TestCase):
    """Test ndh links."""

    public_views = {
        TestModel: ["detail", "update", "list", "create", "absolute"],
        TestModelList: ["list", "absolute"],
        TestModelPK: ["detail", "absolute"],
    }
    private_views = {
        TestModel: ["delete", "admin"],
        TestModelList: ["admin"],
        TestModelPK: ["admin"],
    }

    def setUp(self):
        """Create dummy objects."""
        TestModel.objects.create(name="Hey", moment=timezone.now())
        TestModelList.objects.create(name="Ho", moment=timezone.now())
        TestModelPK.objects.create()


class TestNDH(TestCase):
    """Main class to test ndh functionnalities."""

    def test_models(self):
        """Test ndh.models."""
        # test creation
        self.assertEqual(TestModel.objects.count(), 0)
        TestModel.objects.create(name="Pipo 22 é@ü", moment=timezone.now())
        self.assertEqual(TestModel.objects.count(), 1)

        # test name & slug
        instance = TestModel.objects.first()
        self.assertEqual(instance.name, str(instance))
        self.assertEqual(instance.slug, "pipo-22-eu")

        # test datetimes
        self.assertLess(timezone.now() - instance.created, timedelta(seconds=5))
        almost_zero = instance.updated - instance.created
        self.assertLess(timedelta(0), almost_zero)
        self.assertLess(almost_zero, timedelta(seconds=1))
        instance.save()
        self.assertLess(almost_zero, instance.updated - instance.created)

        # test links
        full = "https://example.com"
        self.assertEqual(instance.get_absolute_url(), f"/test/{instance.slug}")
        self.assertEqual(instance.get_full_url(), f"{full}/test/{instance.slug}")
        self.assertEqual(
            str(instance.get_link()),
            f'<a href="/test/{instance.slug}">{instance}</a>',
        )
        self.assertEqual(
            str(instance.get_md_link()),
            f"[{instance}](/test/{instance.slug})",
        )
        self.assertEqual(
            str(instance.get_full_link()),
            f'<a href="{full}/test/{instance.slug}">{instance}</a>',
        )
        self.assertEqual(
            str(instance.get_full_md_link()),
            f"[{instance}]({full}/test/{instance.slug})",
        )
        self.assertEqual(instance.get_admin_url(), "/admin/testapp/testmodel/1/change/")
        self.assertEqual(
            instance.get_full_admin_url(),
            f"{full}/admin/testapp/testmodel/1/change/",
        )
        self.assertEqual(instance.get_create_url(), "/test/create")
        self.assertEqual(instance.get_delete_url(), "/test/pipo-22-eu/delete")
        self.assertEqual(instance.get_detail_url(), "/test/pipo-22-eu")
        self.assertEqual(instance.get_list_url(), "/test/")
        self.assertEqual(instance.get_update_url(), "/test/pipo-22-eu/update")

        self.assertEqual(TestModel.get_create_url(), "/test/create")
        self.assertEqual(TestModel.get_list_url(), "/test/")

        # test query_sum
        self.assertEqual(query_sum(TestModel.objects.all(), "tests"), 42)
        self.assertEqual(
            query_sum(
                TestModel.objects.all(),
                "tests_decimal",
                output_field=models.DecimalField(),
            ),
            Decimal("3.14"),
        )
        # test ordering
        first = TestModel.objects.create(name="Abc", moment=timezone.now())
        self.assertFalse(TestModel.objects.all().ordered)
        self.assertTrue(TestModel.objects.name_ordered().ordered)
        self.assertEqual(TestModel.objects.name_ordered().first(), first)

    def test_templatetags(self):
        """Test ndh.templatetags."""
        User.objects.create_user(
            username="test",
            password="test",
            first_name="test",
            last_name="test",
            email="test@example.org",
        )

        r = self.client.get(reverse("test"))
        self.assertEqual(r.status_code, 200)
        mail = 'test<span class="at"></span>example<span class="dot"></span>org'
        self.assertIn(mail, r.content.decode())
        self.client.login(username="test", password="test")

        r = self.client.get(reverse("test"))
        self.assertEqual(r.status_code, 200)
        mail = '<span class="mail">'
        mail += '<a  href="mailto:test@example.org">test@example.org</a></span>'
        self.assertIn(mail, r.content.decode())

        User.objects.create_user(username="super", password="super", is_superuser=True)
        self.client.login(username="super", password="super")

        TestModel.objects.create(name="Pipo 22 é@ü", moment=timezone.now())

        r = self.client.get(reverse("testapp:testmodels"))
        self.assertIn("/admin/testapp/testmodel/", r.content.decode())

        r = self.client.get(TestModel.objects.first().get_absolute_url())
        self.assertIn("/admin/testapp/testmodel/1/change", r.content.decode())

        # test navbar_item
        r = self.client.get(reverse("testapp:testmodels"))
        self.assertIn(
            "\n".join(
                [
                    '<li class="nav-item me-auto active">'
                    '<a class="nav-link" href="/test/">List</a></li>',
                    '<li class="nav-item me-auto ">'
                    '<a class="nav-link" href="/test/create">Create</a></li>',
                ],
            ),
            r.content.decode(),
        )
        r = self.client.get(reverse("testapp:testmodel-add"))
        self.assertIn(
            "\n".join(
                [
                    '<li class="nav-item me-auto ">'
                    '<a class="nav-link" href="/test/">List</a></li>',
                    '<li class="nav-item me-auto active">'
                    '<a class="nav-link" href="/test/create">Create</a></li>',
                ],
            ),
            r.content.decode(),
        )
        url = reverse("testapp:user", kwargs={"pk": User.objects.first().pk})
        r = self.client.get(url)
        self.assertIn('Test <span class="smcp">Test</span>', r.content.decode())

    def test_views(self):
        """Test testapp.views."""
        self.assertEqual(TestModel.objects.count(), 0)
        r = self.client.get(reverse("testapp:testmodel-add"))
        self.assertEqual(r.status_code, 200)
        data = {
            "name": "Pipè",
            "tests": 3,
            "moment_0": "2017-12-06",
            "moment_1": "03:19:45",
            "datalist": "toto",
        }
        r = self.client.post(reverse("testapp:testmodel-add"), data)

        self.assertIn(r.content.decode(), "Create Test")
        self.assertEqual(TestModel.objects.count(), 1)

        r = self.client.get(
            reverse("testapp:testmodel-delete", args=[TestModel.objects.first().slug]),
        )
        self.assertEqual(r.status_code, 302)

        User.objects.create_user(username="super", password="super", is_superuser=True)
        self.client.login(username="super", password="super")

        r = self.client.get(
            reverse("testapp:testmodel-delete", args=[TestModel.objects.first().slug]),
        )
        self.assertEqual(r.status_code, 200)

        self.assertEqual(TestModel.objects.count(), 1)

        r = self.client.post(
            reverse("testapp:testmodel-delete", args=[TestModel.objects.first().slug]),
        )
        self.assertEqual(r.status_code, 302)

        self.assertEqual(TestModel.objects.count(), 0)

    def test_absolute_url_list(self):
        """Test ndh.models's get_absolute_url for lists."""
        instance = TestModelList.objects.create(
            name="Pipo 22 é@ü",
            moment=timezone.now(),
        )
        self.assertEqual(instance.get_absolute_url(), reverse("testapp:testmodellists"))

    def test_absolute_url_pk(self):
        """Test ndh.models's get_absolute_url for objects."""
        instance = TestModelPK.objects.create()
        self.assertEqual(instance.get_absolute_url(), f"/test/pk/{instance.pk}")

    def test_utils(self):
        """Test ndh.utils."""
        key = "DJANGO_TEST_GET_ENV"
        val = "it=works"
        no_key = "KEY_WITHOUT_VAL"
        env_file = Path(".env")
        get_env(env_file)
        if key in os.environ:
            val = os.environ[key]
        else:
            with env_file.open("a") as f:
                print(f"{key}={val}", file=f)
        with env_file.open("a") as f:
            print(no_key, file=f)
        get_env(env_file)
        self.assertIn(key, os.environ)
        self.assertEqual(os.environ[key], val)
        self.assertNotIn(no_key, os.environ)

        # Clean the file
        with env_file.open() as f:
            lines = f.readlines()
        with env_file.open("w") as f:
            f.write(
                "\n".join(
                    line
                    for line in lines
                    if not line.startswith(key) and not line.startswith(no_key)
                ),
            )

    def test_context_processors(self):
        """Test ndh.context_processors."""
        self.assertNotIn(
            "UTC",
            self.client.get(reverse("testapp:settings")).content.decode(),
        )
        with self.settings(NDH_TEMPLATES_SETTINGS=["TIME_ZONE"]):
            self.assertIn(
                "UTC",
                self.client.get(reverse("testapp:settings")).content.decode(),
            )

    def test_continue_edit(self):
        """Test NDHFormMixin.continue_edit."""
        TestModel.objects.create(name="a", moment=timezone.now())
        url = reverse("testapp:testmodel-update", kwargs={"slug": "a"})
        data = {
            "name": "a",
            "tests": 314,
            "moment_0": "2017-12-06",
            "moment_1": "03:19:45",
            "datalist": "toto",
        }
        r = self.client.post(url, data)
        self.assertEqual(TestModel.objects.first().tests, 314)
        self.assertEqual(r.status_code, 302)
        self.assertEqual(r.url, "/test/a")
        data["tests"] = 420
        r = self.client.post(f"{url}?continue_edit", data)
        self.assertEqual(TestModel.objects.first().tests, 420)
        self.assertEqual(r.status_code, 302)
        self.assertEqual(r.url, url)
