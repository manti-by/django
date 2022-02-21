from django import template

register = template.Library()


@register.filter(name="cut_text")
def cut_text(text, length):
    return text[:length]
