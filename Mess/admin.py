# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import MessFeedback ,Refund,BankDetails
admin.site.register(MessFeedback)
admin.site.register(Refund)
admin.site.register(BankDetails)

# Register your models here.
