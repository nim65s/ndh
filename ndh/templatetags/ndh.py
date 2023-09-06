"""Django template tags for NDH."""

from django import template
from django.db.models.query import QuerySet
from django.urls import reverse
from django.utils.safestring import mark_safe

register = template.Library()


EMAIL_JS = """<script>
{
   const end = '{end}';
   const start = '{start}';
   const both = start + '@' + end;
   const link = '<a href="mailto:' + both  + '">' + both + '</a>';
   document.write(link);
}
</script>
<noscript>{noscript}</noscript>
"""


TEL_JS = """<script>
{
   const num = '{phone}';
   const link = '<a href="tel:' + num  + '">' + num + '</a>';
   document.write(link);
}
</script>
<noscript>{phone}</noscript>
"""


@register.simple_tag(takes_context=True)
def show_email(context: dict, mail: str) -> str:
    """Show an email as a link to connected users, and obfuscated for others."""
    if context["request"].user.is_authenticated:
        content = f'<a href="mailto:{mail}">{mail}</a>'
    else:
        start, end = mail.split("@")
        at, dot = (f'<span class="{tag}"></span>' for tag in ("at", "dot"))
        noscript = mail.replace("@", at).replace(".", dot)
        content = EMAIL_JS.format(start=start, end=end, noscript=noscript)
    return mark_safe(f'<span class="mail">{content}</span>')


@register.simple_tag(takes_context=True)
def show_phone(context: dict, phone: str) -> str:
    """Show phone number as a link to connected users, and obfuscated for others."""
    if context["request"].user.is_authenticated:
        content = f'<a href="tel:{phone}">{phone}</a>'
    else:
        content = TEL_JS.format(phone=phone)
    return mark_safe(f'<span class="phone">{content}</span>')


@register.filter
def admin_url(obj) -> str:
    """Get the admin url of a Model or QuerySet instance."""
    if isinstance(obj, QuerySet):  # type: ignore
        obj = obj[0]._meta
        return reverse(f"admin:{obj.app_label}_{obj.model_name}_changelist")
    if hasattr(obj, "_queryset_class"):
        obj = obj.first()._meta
        return reverse(f"admin:{obj.app_label}_{obj.model_name}_changelist")
    return reverse(
        f"admin:{obj._meta.app_label}_{obj._meta.model_name}_change",
        args=[obj.pk],
    )


@register.simple_tag(takes_context=True)
def navbar_item(context, view_name: str, link: str) -> str:
    """Get a navbar item, activated if its url is in the current request path."""
    url = reverse(view_name)
    active = "active" if url == context.request.path else ""
    return mark_safe(
        f'<li class="nav-item me-auto {active}">'
        f'<a class="nav-link" href="{url}">{link}</a></li>',
    )


@register.filter
def user_smcp(user):
    """Get user's capitalized `first_name` + capitalized & small-capsed `last_name`."""
    return mark_safe(
        f"{user.first_name.capitalize()} "
        f'<span class="smcp">{user.last_name.capitalize()}</span>',
    )
