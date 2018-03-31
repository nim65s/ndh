from django.urls import path
from django.views.generic import DetailView, ListView, TemplateView

from . import views
from .models import TestModel, TestModelList, TestModelPK

CTX = {'email': 'test@example.org'}

app_name = 'testapp'
urlpatterns = [
    path('', ListView.as_view(model=TestModel), name='testmodels'),
    path('create', views.TestCreateView.as_view(), name='testmodel-add'),
    path('list', ListView.as_view(model=TestModelList), name='testmodellists'),
    path('pk/<int:pk>', DetailView.as_view(model=TestModelPK), name='testmodelpk'),
    path('settings', TemplateView.as_view(template_name='testapp/settings.html'), name='settings'),
    path('<slug:slug>', DetailView.as_view(model=TestModel), name='testmodel'),
    path('<slug:slug>/delete', views.TestDeleteView.as_view(), name='testmodel-del'),
]
