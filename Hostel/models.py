# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from datetime import datetime 
from django.contrib.auth.models import AbstractUser
from datetime import datetime
class User(AbstractUser):
    is_student = models.BooleanField(default=False)
    is_employee = models.BooleanField(default=False)

class Student(models.Model):
	user=models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
	first_name=models.CharField(max_length=50,default=None,null=True)
	rollno=models.CharField(max_length=50,default=None,unique=True)
	middle_name=models.CharField(max_length=50,default=None,null=True)
	last_name=models.CharField(max_length=50,default=None,null=True)
	regis_year=models.IntegerField(default=None,null=True)
	gender=models.CharField(max_length=2,null=True)
	curr_year=models.IntegerField(default=None,null=True)
	regis_deg=models.CharField(max_length=20,default=None,null=True)
	regis_deg_dur=models.IntegerField(default=None,null=True)
	curr_sem=models.IntegerField(default=None,null=True)
	blood_grp=models.CharField(max_length=20,default=None,null=True)
	def __str__(self):
		return str(self.rollno)


class MobileNo(models.Model):
	user=models.ForeignKey(User,on_delete=models.CASCADE)
	mobile_no=models.CharField(max_length=20)


class RoomRegistration(models.Model):
	student=models.OneToOneField(Student,on_delete=models.CASCADE,default=None)
	pref_room_no=models.IntegerField(default=0)
	fee_proof=models.FileField(default=None)
	hostel_name=models.CharField(max_length=10,default=None)
	def __str__(self):
		return str(self.student)+','+str(self.pref_room_no)+','+str(self.fee_proof)+','+str(self.hostel_name)

class HostelComplaint(models.Model):
	student=models.ForeignKey(Student,on_delete=models.CASCADE,default=None)
	complaint=models.CharField(max_length=500,default=None)
	complain_time=models.DateTimeField(default=datetime.now)
	def __str__(self):
		return str(self.student)+','+str(self.complaint)+','+str(self.complain_time)

class InOutList(models.Model):
	student=models.ForeignKey(Student,on_delete=models.CASCADE,default=None)
	in_time=models.CharField(default=None,max_length=200)
	out_time=models.CharField(default=None,max_length=200)
	out_reason=models.CharField(max_length=500,default=None)
	out_place=models.CharField(max_length=15,default=None)
	is_out=models.BooleanField(default=False)


class GuestEntry(models.Model):
	student=models.ForeignKey(Student,on_delete=models.CASCADE,default=None)
	guest_gender=models.CharField(max_length=2)
	no_of_stay=models.IntegerField(default=None)
	guest_name=models.CharField(max_length=100,default=None)
	guest_age=models.IntegerField(default=None)


class Employee(models.Model):
	user=models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
	first_name=models.CharField(max_length=50,default=None)
	middle_name=models.CharField(max_length=50,default=None)
	last_name=models.CharField(max_length=50,default=None)
	gender=models.CharField(max_length=2)
	joining_year=models.CharField(max_length=10)
	blood_grp=models.CharField(max_length=20,default=None)
	role=models.CharField(max_length=10)
	department=models.CharField(max_length=10)

	
