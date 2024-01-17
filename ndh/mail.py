"""Utils for email display."""
from django.utils.safestring import mark_safe

EMAIL_JS = """<script>
{{
   const end = '{end}';
   const start = '{start}';
   const both = start + '@' + end;
   const link = '<a href="mailto:' + both  + '">' + {text} + '</a>';
   document.write(link);
}}
</script>
<noscript>{noscript}</noscript>
"""


def show_emails(authenticated: bool, *mails: [str], text: str = "") -> str:
    """Show an email as a link to connected users, and obfuscated for others."""
    mail = mails[0]
    if authenticated:
        content = f'<a href="mailto:{mail}">{text or mail}</a>'
    else:
        start, end = mail.split("@")
        at, dot = (f'<span class="{tag}"></span>' for tag in ("at", "dot"))
        noscript = mail.replace("@", at).replace(".", dot)
        content = EMAIL_JS.format(
            start=start,
            end=end,
            noscript=noscript,
            text=f'"{text}"' if text else "both",
        )
    return mark_safe(f'<span class="mail">{content}</span>')
