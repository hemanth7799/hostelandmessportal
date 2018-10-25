# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from datetime import datetime 

# Create your models here.
class Student(models.Model):
	roll_no=models.CharField(max_length=15,default='')
	first_name=models.CharField(max_length=50,default='')
	middle_name=models.CharField(max_length=50,default='')
	last_name=models.CharField(max_length=50,default='')
	regis_year=models.IntegerField(default='2016')
	gender=models.CharField(max_length=1)
	curr_year=models.IntegerField(default=3)
	regis_deg=models.CharField(max_length=20,default='B.Tech')
	regis_deg_dur=models.IntegerField(default=3)
	curr_sem=models.IntegerField(default=7)
	blood_grp=models.CharField(max_length=20,default='B-')
	email=models.EmailField(default='example@iiits.in')
	def __str__(self):
		return self.roll_no
class MobileNo(models.Model):
	student=models.ForeignKey(Student, on_delete=models.CASCADE,default=0)
	mobile_no=models.CharField(max_length=10,default=0)
class RoomRegistration(models.Model):
	roll_no=models.CharField(max_length=15,default='')
	room_no=models.IntegerField(default=0)
	fee_proof=models.FileField()
	hostel_name=models.CharField(max_length=10,default='')
class HostelComplaint(models.Model):
	roll_no=models.CharField(max_length=15,default='')
	complaint=models.CharField(max_length=500,default='')
	complain_time=models.DateTimeField(default=datetime.now)
class InOutList(models.Model):
	roll_no=models.CharField(max_length=15,default='')
	in_time=models.DateTimeField(default=datetime.now)
	out_time=models.DateTimeField(default=datetime.now)
	out_reason=models.CharField(max_length=500,default='')
	out_place=models.CharField(max_length=15,default='')
class GuestEntry(models.Model):
	roll_no=models.CharField(max_length=15,default='')
	guest_gender=models.CharField(max_length=1)
	no_of_stay=models.IntegerField(default=0)



	
	
