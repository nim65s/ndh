from django import template

register = template.Library()


@register.filter
def email(email, request):
    if request.user.is_authenticated():
        content = '<a href="mailto:%s">%s</a>' % (email, email)
    else:
        at, dot = ('<span class="%s"></span>' % i for i in ['at', 'dot'])
        content = email.replace('@', at).replace('.', dot)
    return mark_safe('<span class="mail">%s</span>' % content)

