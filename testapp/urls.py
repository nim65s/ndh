from django.contrib import admin
from django.urls import include, path
from django.views.generic import DetailView, ListView, TemplateView

from . import views
from .models import TestModel

CTX = {'email': 'test@example.org'}

app_name = 'testapp'
urlpatterns = [
    path('', ListView.as_view(model=TestModel), name='testmodels'),
    path('create', views.TestCreateView.as_view(), name='testmodel-add'),
    path('<slug:slug>', DetailView.as_view(model=TestModel), name='testmodel'),
    path('<slug:slug>/delete', views.TestDeleteView.as_view(), name='testmodel-del'),
]
