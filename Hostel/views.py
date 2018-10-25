# -*- coding: utf-8 -*-
# Create your views here.
from __future__ import unicode_literals
from Hostel.models import Student,MobileNo,RoomRegistration,HostelComplaint,InOutList,GuestEntry
from django.http import Http404
from django.shortcuts import get_object_or_404,render
# Create your views here.
from django.http import HttpResponse
def inOutIndex(request):
	form={}
  # if this is a POST request we need to process the form data
	if request.method == 'POST':
    # create a form instance and populate it with data from the request:
		in_time= request.POST['in_time']
		out_time = request.POST['out_time']
		out_place=request.POST['out_place']
		out_reason=request.POST['out_reason']
		
		roomregistration=RoomRegistration()
		roomregistration.in_time=in_time
		roomregistration.out_time=out_time
		roomregistration.out_place=out_place
		roomregistration.out_reason=out_reason
		roomregistration.save()
		return HttpResponseRedirect('/dashboard/1')
	context={'text':0}
			
	return render(request, 'rasp/add.html',context)
	


