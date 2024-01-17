"""Utils for email display."""

from django.contrib.auth import get_user_model
from django.utils.safestring import mark_safe

User = get_user_model()

AT, DOT = (f'<span class="{tag}"></span>' for tag in ("at", "dot"))
EMAIL_JS = """<script>
{{
   const mails = {mails}.map((m) => m.join('@')).join();
   const link = '<a href="mailto:' + mails + {subject} + '">' + {text} + '</a>';
   document.write(link);
}}
</script>
<noscript>{noscript}</noscript>
"""


def show_emails(
    authenticated: bool,
    *to: [User | str],
    text: str = "",
    subject: str = "",
) -> str:
    """Show an email as a link to connected users, and obfuscated for others."""
    mails = [p.email if isinstance(p, User) else p for p in to]
    if authenticated:
        subject = f"?subject={subject}" if subject else ""
        mails = ",".join(mails)
        content = f'<a href="mailto:{mails}{subject}">{text or mails}</a>'
    else:
        subject = f"'?subject={subject}'" if subject else "''"
        noscript = ",".join(mails).replace("@", AT).replace(".", DOT)
        content = EMAIL_JS.format(
            mails=[m.split("@") for m in mails],
            noscript=noscript,
            text=f"'{text}'" if text else "mails",
            subject=subject,
        )
    return mark_safe(f'<span class="mail">{content}</span>')
