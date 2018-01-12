from django.contrib import admin
from django.urls import include, path
from django.views.generic import DetailView, ListView, TemplateView

from . import views
from .models import TestModel

CTX = {'email': 'test@example.org'}

urlpatterns = [
    path(r'admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', TemplateView.as_view(template_name='base.html', extra_context=CTX), name='test'),
    path('test/', ListView.as_view(model=TestModel), name='list'),
    path('test/create', views.TestCreateView.as_view(), name='create'),
    path('test/<str:slug>', DetailView.as_view(model=TestModel), name='detail'),
    path('test/<str:slug>/delete', views.TestDeleteView.as_view(), name='delete'),
]
