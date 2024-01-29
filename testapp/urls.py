"""Define URLs for the test app."""

from django.contrib.auth.models import User
from django.urls import path
from django.views.generic import DetailView, ListView, TemplateView

from . import views
from .models import TestModel, TestModelList, TestModelPK

app_name = "testapp"
urlpatterns = [
    path("", ListView.as_view(model=TestModel), name="testmodels"),
    path("create", views.TestCreateView.as_view(), name="testmodel-add"),
    path("list", ListView.as_view(model=TestModelList), name="testmodellists"),
    path("user/<int:pk>", DetailView.as_view(model=User), name="user"),
    path("pk/<int:pk>", DetailView.as_view(model=TestModelPK), name="testmodelpk"),
    path(
        "settings",
        TemplateView.as_view(template_name="testapp/settings.html"),
        name="settings",
    ),
    path("<slug:slug>", DetailView.as_view(model=TestModel), name="testmodel"),
    path("<slug:slug>/update", views.TestUpdateView.as_view(), name="testmodel-update"),
    path("<slug:slug>/delete", views.TestDeleteView.as_view(), name="testmodel-delete"),
]
