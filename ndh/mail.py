"""Utils for email display."""

from collections.abc import Iterable

from django.contrib.auth import get_user_model
from django.utils.safestring import mark_safe

User = get_user_model()

AT, DOT = (f'<span class="{tag}"></span>' for tag in ("at", "dot"))
EMAIL_JS = """<script>
{{
   const mails = {mails}.map((m) => m.join('@')).join();
   const link = '<a {klass} href="mailto:' + mails + {subject} + '">' + {text} + '</a>';
   document.write(link);
}}
</script>
<noscript>{noscript}</noscript>
"""


def flatten(iterable):
    """Flatten an iterable of "values or iterables"."""
    return (
        [c for b in iterable for c in flatten(b)]
        if isinstance(iterable, Iterable) and not isinstance(iterable, str)
        else [iterable]
    )


def show_emails(
    authenticated: bool,
    *to: [User | str],
    text: str = "",
    subject: str = "",
    klass: str = "",
) -> str:
    """Show an email as a link to authenticated users, and obfuscated for others."""
    mails = [r.email if hasattr(r, "email") else r for r in flatten(to)]
    subject = f"?subject={subject}" if subject else ""
    klass = f'class="{klass}"' if klass else ""
    if authenticated:
        mails = ",".join(mails)
        content = f'<a {klass} href="mailto:{mails}{subject}">{text or mails}</a>'
    else:
        content = EMAIL_JS.format(
            mails=[m.split("@") for m in mails],
            noscript=",".join(mails).replace("@", AT).replace(".", DOT),
            text=f"'{text}'" if text else "mails",
            subject=f"'{subject}'",
            klass=klass,
        )
    return mark_safe(f'<span class="mail">{content}</span>')
