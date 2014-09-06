from django import template
register = template.Library()


@register.filter(name='add_class')
def add_class(field, klass):
    return field.as_widget(attrs={"class": klass})
