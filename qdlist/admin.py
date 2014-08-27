# coding=utf-8
__author__ = 'taksenov'

from django.contrib import admin
from qdlist.models import *

admin.site.register(type)
admin.site.register(subtype)
admin.site.register(name)
admin.site.register(links)
admin.site.register(quantizeddoc)