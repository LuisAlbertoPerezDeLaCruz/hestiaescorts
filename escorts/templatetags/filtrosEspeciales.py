# -*- coding: utf-8 -*-
from django import template
register = template.Library()

def phone_number(number):
    """Convert a 11 character string into (xxx) xxx-xxxx."""
    first = number[0:4]
    second = number[4:7]
    third = number[7:11]
    return '(' + first + ')' + ' ' + second + '-' + third

register.filter('phone_number', phone_number)