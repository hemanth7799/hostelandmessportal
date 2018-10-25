# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from Hostel.models import Student,MobileNo,RoomRegistration,HostelComplaint,InOutList,GuestEntry,Employee

admin.site.register(Student)
admin.site.register(MobileNo)
admin.site.register(RoomRegistration)
admin.site.register(HostelComplaint)
admin.site.register(InOutList)
admin.site.register(GuestEntry)
admin.site.register(Employee)
