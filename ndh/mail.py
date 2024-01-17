"""Utils for email display."""

from django.utils.safestring import mark_safe

EMAIL_JS = """<script>
{{
   const mails = {mails}.map((m) => m.join('@')).join();
   const link = '<a href="mailto:' + mails  + '">' + {text} + '</a>';
   document.write(link);
}}
</script>
<noscript>{noscript}</noscript>
"""


def show_emails(authenticated: bool, *mails: [str], text: str = "") -> str:
    """Show an email as a link to connected users, and obfuscated for others."""
    if authenticated:
        mails = ",".join(mails)
        content = f'<a href="mailto:{mails}">{text or mails}</a>'
    else:
        at, dot = (f'<span class="{tag}"></span>' for tag in ("at", "dot"))
        noscript = ",".join(mails).replace("@", at).replace(".", dot)
        content = EMAIL_JS.format(
            mails=[m.split("@") for m in mails],
            noscript=noscript,
            text=f"'{text}'" if text else "mails",
        )
    return mark_safe(f'<span class="mail">{content}</span>')
