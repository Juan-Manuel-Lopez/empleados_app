from django import template
register = template.Library()

def cut_jm(value,arg):
    """
    description
    """
    return value.replace(arg,'')

register.filter('cut_jm',cut_jm)
