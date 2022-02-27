"""Main URLS for the test project."""
from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView

CTX = {"email": "test@example.org"}

urlpatterns = [
    path(r"admin/", admin.site.urls),
    path("accounts/", include("django.contrib.auth.urls")),
    path("i18n/", include("django.conf.urls.i18n")),
    path(
        "",
        TemplateView.as_view(template_name="base.html", extra_context=CTX),
        name="test",
    ),
    path("test/", include("testapp.urls")),
]
