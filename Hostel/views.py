# -*- coding: utf-8 -*-
# Create your views here.
from __future__ import unicode_literals
from Hostel.models import Student,MobileNo,RoomRegistration,HostelComplaint,InOutList,GuestEntry
from django.http import Http404
from django.shortcuts import get_object_or_404,render
# Create your views here.
from django.http import HttpResponse
from django.contrib.auth.models import User
def inOutIndex(request):
	form={}
  # if this is a POST request we need to process the form data
	if request.method == 'POST':
    # create a form instance and populate it with data from the request:
		in_time= request.POST['in_time']
		out_time = request.POST['out_time']
		out_place=request.POST['out_place']
		out_reason=request.POST['out_reason']
		usr=User.objects.get(username='lokesh')
		stud=Student()
		stud.user=usr
		stud.rollno='S20160010078'
		stud.save()
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
		usr=User.objects.get(username='lokesh')
		stud=Student()
		stud.user=usr
		stud.rollno='S20160010078'
		stud.save()
		hos_compl=HostelComplaint()
		hos_compl.complaint=complaint
		hos_complain_time=complain_time

		hos_compl.save()
		return HttpResponse('data stored in db')
	context={'text':0}
			
	return render(request, 'Hostel/hostelcomplaint.html',context)

	


