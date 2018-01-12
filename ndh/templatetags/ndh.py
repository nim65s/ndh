from django import template
from django.db.models.query import QuerySet
from django.urls import reverse
from django.utils.safestring import mark_safe

register = template.Library()


@register.simple_tag(takes_context=True)
def show_email(context, mail):
    request = context['request']
    if request.user.is_authenticated:
        content = f'<a href="mailto:{mail}">{mail}</a>'
    else:
        at, dot = (f'<span class="{tag}"></span>' for tag in ('at', 'dot'))
        content = mail.replace('@', at).replace('.', dot)
    return mark_safe(f'<span class="mail">{content}</span>')


@register.filter
def admin_url(obj):
    if isinstance(obj, QuerySet):
        obj = obj[0]._meta
        return reverse(f'admin:{obj.app_label}_{obj.model_name}_changelist')
    return reverse(f'admin:{obj._meta.app_label}_{obj._meta.model_name}_change', args=[obj.pk])
