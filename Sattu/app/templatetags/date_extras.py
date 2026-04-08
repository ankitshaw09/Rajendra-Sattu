from django import template
from datetime import date

register = template.Library()

@register.simple_tag
def years_since(year):
    current_year = date.today().year
    return current_year - year