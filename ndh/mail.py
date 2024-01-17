"""Utils for email display."""

from django.utils.safestring import mark_safe

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
    *mails: [str],
    text: str = "",
    subject: str = "",
) -> str:
    """Show an email as a link to connected users, and obfuscated for others."""
    subject = f"'?subject={subject}'" if subject else "''"
    if authenticated:
        mails = ",".join(mails)
        content = f'<a href="mailto:{mails}{subject}">{text or mails}</a>'
    else:
        noscript = ",".join(mails).replace("@", AT).replace(".", DOT)
        content = EMAIL_JS.format(
            mails=[m.split("@") for m in mails],
            noscript=noscript,
            text=f"'{text}'" if text else "mails",
            subject=subject,
        )
    return mark_safe(f'<span class="mail">{content}</span>')
