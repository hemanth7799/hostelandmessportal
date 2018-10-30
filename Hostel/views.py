# -*- coding: utf-8 -*-
# Create your views here.
from __future__ import unicode_literals
from Hostel.models import Student,MobileNo,RoomRegistration,HostelComplaint,InOutList,GuestEntry,User
from django.http import Http404
from django.shortcuts import get_object_or_404,render
# Create your views here.
from django.http import HttpResponse
#from django.contrib.auth.models import AbstractUser
def inOutIndex(request):
	form={}
  # if this is a POST request we need to process the form data
	if request.method == 'POST':
    # create a form instance and populate it with data from the request:
		in_time= request.POST['in_time']
		out_time = request.POST['out_time']
		out_place=request.POST['out_place']
		out_reason=request.POST['out_reason']
		usr=User.objects.get(username='venkatlokesh')
		stud=Student()
		stud=Student.objects.get(user=usr)
		
		in_out=InOutList()
		in_out.student=stud
		in_out.in_time=in_time
		in_out.out_time=out_time
		in_out.out_place=out_place
		in_out.out_reason=out_reason
		in_out.save()
		return HttpResponse('data stored in db')
	context={'text':0}
			
	return render(request, 'Hostel/inout.html',context)
def HostelComplaintIndex(request):
	form={}
  # if this is a POST request we need to process the form data
	if request.method == 'POST':
    # create a form instance and populate it with data from the request:
		complain_time= request.POST['complain_time']
		
		complaint=request.POST['complaint']
		usr=User.objects.get(username='venkatlokesh')
		stud=Student()
		stud=Student.objects.get(user=usr)
		#stud.save()
		hos_compl=HostelComplaint()
		hos_compl.student=stud
		hos_compl.complaint=complaint
		hos_compl.complain_time=complain_time

		hos_compl.save()
		return HttpResponse('data stored in db')
	context={'text':0}
			
	return render(request, 'Hostel/hostelcomplaint.html',context)
def GuestEntryIndex(request):
	form={}
  # if this is a POST request we need to process the form data
	if request.method == 'POST':
    # create a form instance and populate it with data from the request:
		guest_gender= request.POST['guest_gender']
		guest_name = request.POST['guest_name']
		guest_age=request.POST['guest_age']
		no_of_days=request.POST['no_of_stay']
		usr=User.objects.get(username='venkatlokesh')
		stud=Student()
		stud=Student.objects.get(user=usr)
		
		guest_entry=GuestEntry()
		guest_entry.student=stud
		guest_entry.guest_gender=guest_gender
		guest_entry.guest_name=guest_name
		guest_entry.guest_age=guest_age
		guest_entry.no_of_stay=no_of_days
		guest_entry.save()
		return HttpResponse('data stored in db')
	context={'text':0}
			
	return render(request, 'Hostel/guestEntry.html',context)

