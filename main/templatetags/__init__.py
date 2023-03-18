from django import template
from . import custom_filters

register = template.Library()

register.filter('base64', custom_filters.base64)