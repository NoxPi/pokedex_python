from django import template

register = template.Library()


@register.filter(name='type_to_label')
def type_to_label(p_type):
    return '<span class="label ' + p_type.name.lower() + '">' + p_type.name + '</span>'
