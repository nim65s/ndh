"""Django template tags for NDH."""

from django import template
from django.contrib.auth import get_user_model
from django.db.models.query import QuerySet
from django.urls import reverse
from django.utils.safestring import mark_safe

from ndh.mail import show_emails

User = get_user_model()

register = template.Library()


TEL_JS = """<script>
{{
   const num = '{phone}';
   const num_nosp = '{phone_nosp}';
   const link = '<a href="tel:' + num_nosp  + '">' + num + '</a>';
   document.write(link);
}}
</script>
<noscript>{phone}</noscript>
"""


@register.simple_tag(takes_context=True)
def show_email(
    context: dict,
    *to: [User | str],
    text: str = "",
    subject: str = "",
    klass: str = "",
) -> str:
    """Show an email as a link to connected users, and obfuscated for others."""
    return show_emails(
        context["request"].user.is_authenticated,
        *to,
        text=text,
        subject=subject,
        klass=klass,
    )


@register.simple_tag(takes_context=True)
def show_phone(context: dict, phone: str) -> str:
    """Show phone number as a link to connected users, and obfuscated for others."""
    phone_nosp = phone.replace(" ", "").replace("(", "").replace(")", "")
    if context["request"].user.is_authenticated:
        content = f'<a href="tel:{phone_nosp}">{phone}</a>'
    else:
        content = TEL_JS.format(phone=phone, phone_nosp=phone_nosp)
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
def user_smcp(user: User):
    """Get user's capitalized `first_name` + capitalized & small-capsed `last_name`."""
    return mark_safe(
        f"{user.first_name.capitalize()} "
        f'<span class="smcp">{user.last_name.capitalize()}</span>',
    )
