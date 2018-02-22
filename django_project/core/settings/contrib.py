# coding=utf-8
"""
core.settings.contrib
"""
from .base import *  # noqa

STOP_WORDS = (
    'a', 'an', 'and', 'if', 'is', 'the', 'in', 'i', 'you', 'other',
    'this', 'that', 'to',
)

# 3rd party apps
INSTALLED_APPS += (  # noqa : F405
    'rolepermissions',
)
ROLEPERMISSIONS_MODULE = 'roles.settings.roles'
ROLEPERMISSIONS_REGISTER_ADMIN = True
