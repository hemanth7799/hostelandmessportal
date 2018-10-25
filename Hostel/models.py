# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from datetime import datetime 
from django.contrib.auth.models import User
class Student(models.Model):
	user=models.OneToOneField(User,on_delete=models.CASCADE,default=None)
	first_name=models.CharField(max_length=50,default=None)
	rollno=models.CharField(max_length=50,default=None)
	middle_name=models.CharField(max_length=50,default=None)
	last_name=models.CharField(max_length=50,default=None)
	regis_year=models.IntegerField(default=None)
	gender=models.CharField(max_length=2)
	curr_year=models.IntegerField(default=None)
	regis_deg=models.CharField(max_length=20,default=None)
	regis_deg_dur=models.IntegerField(default=None)
	curr_sem=models.IntegerField(default=None)
	blood_grp=models.CharField(max_length=20,default=None)
	def __str__(self):
		return str(self.rollno)
class MobileNo(models.Model):
	user=models.ForeignKey(User,on_delete=models.CASCADE,default=None)
	mobile_no=models.CharField(max_length=20)
class RoomRegistration(models.Model):
	student=models.OneToOneField(Student,on_delete=models.CASCADE,default=None)
	room_no=models.IntegerField(default=0)
	fee_proof=models.FileField()
	hostel_name=models.CharField(max_length=10,default=None)
class HostelComplaint(models.Model):
	student=models.ForeignKey(Student,on_delete=models.CASCADE,default=None)
	complaint=models.CharField(max_length=500,default=None)
	complain_time=models.DateTimeField(default=datetime.now)
class InOutList(models.Model):
	student=models.ForeignKey(Student,on_delete=models.CASCADE,default=None)
	in_time=models.DateTimeField(default=None)
	out_time=models.DateTimeField(default=None)
	out_reason=models.CharField(max_length=500,default=None)
	out_place=models.CharField(max_length=15,default=None)
class GuestEntry(models.Model):
	student=models.ForeignKey(Student,on_delete=models.CASCADE,default=None)
	guest_gender=models.CharField(max_length=2)
	no_of_stay=models.IntegerField(default=None)
class Employee(models.Model):
	user=models.OneToOneField(User,on_delete=models.CASCADE)
	first_name=models.CharField(max_length=50,default=None)
	middle_name=models.CharField(max_length=50,default=None)
	last_name=models.CharField(max_length=50,default=None)
	gender=models.CharField(max_length=2)
	joining_year=models.CharField(max_length=10)
	blood_grp=models.CharField(max_length=20,default=None)
	role=models.CharField(max_length=10)
	department=models.CharField(max_length=10)


	


	
	
