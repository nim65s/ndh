from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView

from . import views

CTX = {'email': 'test@example.org'}

urlpatterns = [
    path(r'admin/', admin.site.urls),
    path(r'test', TemplateView.as_view(template_name='base.html', extra_context=CTX), name='test'),
    path(r'create', views.TestCreateView.as_view(), name='create'),
    path(r'delete/<int:pk>', views.TestDeleteView.as_view(), name='delete'),
]
