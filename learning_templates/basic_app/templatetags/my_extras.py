from django import template

register = template.Library()

@register.filter(name='ccut')
def cut(value, arg):
    return value.replace(arg, '')

# or with decorator, use the following command
# register.filter('cut', cut)
