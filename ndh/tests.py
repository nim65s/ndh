"""Test helpers for NDH."""

from django.contrib.auth import get_user_model
from django.test import TestCase

from ndh.mail import show_emails


class TestMail(TestCase):
    """Test ndh/mail.py module."""

    def test_show_emails(self):
        """Test show_emails function."""
        mail = "abc@def.com"
        text = "text"

        self.assertIn(mail, show_emails(True, mail))
        self.assertNotIn(mail, show_emails(False, mail))
        self.assertIn(mail, show_emails(True, mail, text=text))
        self.assertNotIn(mail, show_emails(False, mail, text=text))
        self.assertIn(text, show_emails(True, mail, text=text))
        self.assertIn(text, show_emails(False, mail, text=text))
        self.assertIn(mail, show_emails(True, mail, mail))
        self.assertNotIn(mail, show_emails(False, mail, mail))
        self.assertIn(mail, show_emails(True, mail, mail, text=text))
        self.assertNotIn(mail, show_emails(False, mail, mail, text=text))
        self.assertIn(text, show_emails(True, mail, mail, text=text))
        self.assertIn(text, show_emails(False, mail, mail, text=text))
        self.assertIn(",".join([mail, mail]), show_emails(True, mail, mail, text=text))


class TestNDHLinks(TestCase):
    """Test the Links abstract model."""

    public_views = {}
    private_views = {}

    def test_links(self):
        """Test public and private views."""

        def creation_message(model):
            return (
                f"You need to create a {model.__module__}.{model.__name__} in the setUp"
                f" method of {self.__class__.__module__}.{self.__class__.__name__}."
            )

        for model, views in self.public_views.items():
            instance = model.objects.first()
            self.assertIsNotNone(instance, creation_message(model))
            for view in views:
                r = self.client.get(getattr(instance, f"get_{view}_url")())
                self.assertEqual(r.status_code, 200, f"{model=} {view=} {r=}")

        for model, views in self.private_views.items():
            instance = model.objects.first()
            self.assertIsNotNone(instance, creation_message(model))
            for view in views:
                r = self.client.get(getattr(instance, f"get_{view}_url")())
                self.assertEqual(r.status_code, 302, f"{model=} {view=} {r=}")

        get_user_model().objects.create_user(
            username="ndh_test_links",
            password="ndh_test_links",
            is_staff=True,
            is_superuser=True,
        )
        self.client.login(username="ndh_test_links", password="ndh_test_links")

        for model, views in self.private_views.items():
            instance = model.objects.first()
            self.assertIsNotNone(instance, creation_message(model))
            for view in views:
                r = self.client.get(getattr(instance, f"get_{view}_url")())
                self.assertEqual(r.status_code, 200, f"{model=} {view=} {r=}")
