# -*- coding: utf-8 -*-
from django import template
from django.utils.text import Truncator
from ..models import *
register = template.Library()

def phone_number(number):
    """Convert a 11 character string into (xxx) xxx-xxxx."""
    first = number[0:4]
    second = number[4:7]
    third = number[7:11]
    return '(' + first + ')' + ' ' + second + '-' + third

register.filter('phone_number', phone_number)

def truncatereadmore(value, arg):
    """
    Truncates a string after a certain number of words.

    Argument: Number of words to truncate after.

    Newlines within the string are removed.
    """
    try:
        length = arg
    except ValueError: # Invalid literal for int().
        return value # Fail silently.
    return Truncator(value).words(length, truncate=' ...')

register.filter('truncatereadmore', truncatereadmore)

@register.simple_tag
def tieneEstaCaracteristica(escortId,caracteristicaId):
    return CaracteristicasEscort.objects.filter(ce_escort_id=escortId,ce_caracteristica_id=caracteristicaId).exists()

