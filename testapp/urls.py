from django.urls import path
from django.views.generic import DetailView, ListView

from . import views
from .models import TestModel, TestModelList

CTX = {'email': 'test@example.org'}

app_name = 'testapp'
urlpatterns = [
    path('', ListView.as_view(model=TestModel), name='testmodels'),
    path('create', views.TestCreateView.as_view(), name='testmodel-add'),
    path('<slug:slug>', DetailView.as_view(model=TestModel), name='testmodel'),
    path('<slug:slug>/delete', views.TestDeleteView.as_view(), name='testmodel-del'),
    path('list', ListView.as_view(model=TestModelList), name='testmodellists'),
]
