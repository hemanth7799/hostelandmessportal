# -*- coding: utf-8 -*-
# Create your views here.
from __future__ import unicode_literals
from Hostel.models import Student,MobileNo,RoomRegistration,HostelComplaint,InOutList,GuestEntry,User
from django.http import Http404
from django.shortcuts import get_object_or_404,render
from django.contrib.auth import authenticate,login
# Create your views here.
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from Hostel.forms import RoomRegistrationForm
#from django.contrib.auth.models import AbstractUser
IMAGE_FILE_TYPES = ['png', 'jpg', 'jpeg','pdf']
def homepage(request):
	return render(request,'Hostel/MyHome.html')
def inOutIndex(request):
	form={}
	if request.user.is_authenticated() :
  # if this is a POST request we need to process the form data
		if request.method == 'POST':
    # create a form instance and populate it with data from the request:
			in_time= request.POST['in_time']
			out_time = request.POST['out_time']
			out_place=request.POST['out_place']
			out_reason=request.POST['out_reason']
			usr=User.objects.get(username=request.user.username)
			stud=Student()
			stud=Student.objects.get(user=usr)
		
			in_out=InOutList()
			in_out.student=stud
			in_out.in_time=in_time
			in_out.out_time=out_time
			in_out.out_place=out_place
			in_out.out_reason=out_reason
			in_out.save()
			#return HttpResponse('data stored in db')
		context={'text':0}
			
		return render(request, 'Hostel/inout.html',context)
	else:
		context={'text':0}
		return render(request, 'Hostel/login.html',context)
def HostelComplaintIndex(request):
	form={}
	if request.user.is_authenticated() :
  # if this is a POST request we need to process the form data
		if request.method == 'POST':
    # create a form instance and populate it with data from the request:
			#complain_time= request.POST['complain_time']
		
			complaint=request.POST['complaint']
			usr=User.objects.get(username=request.user.username)
			stud=Student()
			stud=Student.objects.get(user=usr)
		#stud.save()
			hos_compl=HostelComplaint()
			hos_compl.student=stud
			hos_compl.complaint=complaint
		#hos_compl.complain_time=complain_time

			hos_compl.save()
			#return HttpResponse('data stored in db')
		context={'text':0}
			
		return render(request, 'Hostel/hostelcomplaint.html',context)
	else:
		context={'text':0}
		return render(request, 'Hostel/login.html',context)
def GuestEntryIndex(request):
	form={}
	if (request.user.is_authenticated() ):
  # if this is a POST request we need to process the form data
		if request.method == 'POST':
    # create a form instance and populate it with data from the request:
			guest_gender= request.POST['guest_gender']
			guest_name = request.POST['guest_name']
			guest_age=request.POST['guest_age']
			no_of_days=request.POST['no_of_stay']
			usr=User.objects.get(username=request.user.username)
			stud=Student()
			stud=Student.objects.get(user=usr)
		
			guest_entry=GuestEntry()
			guest_entry.student=stud
			guest_entry.guest_gender=guest_gender
			guest_entry.guest_name=guest_name
			guest_entry.guest_age=guest_age
			guest_entry.no_of_stay=no_of_days
			guest_entry.save()
			#return HttpResponse('data stored in db')
		context={'text':0}
			
		return render(request, 'Hostel/guestEntry.html',context)
	else:
		context={'text':0}
		return render(request, 'Hostel/login.html',context)
def registration_form(request):
	form=RoomRegistrationForm(request.POST or None,request.FILES or None)
	if request.user.is_authenticated() :
		if request.method == 'POST':
			if form.is_valid():
	 			try:
					form = RoomRegistrationForm(request.POST, request.FILES)
					usr=User.objects.get(username=request.user.username)
					stud=Student()
					stud=Student.objects.get(user=usr)
			
			

        		
            			
            				room_no=request.POST.get('pref_room_no')
					hos_name=request.POST.get('hostel_name')
					if(len(RoomRegistration.objects.filter(pref_room_no=room_no))>1 and len(RoomRegistration.objects.filter(hostel_name=hos_name))>1 ):
						return HttpResponseRedirect('/hostel/roomregistration')
	   				roomregis=RoomRegistration()
	    				roomregis.pref_room_no=room_no
	    				roomregis.fee_proof=request.FILES.get('fee_proof')
	    				roomregis.hostel_name=hos_name
	    				roomregis.student=stud
					file_type = roomregis.fee_proof.url.split('.')[-1]
            				file_type = file_type.lower()
           				if file_type not in IMAGE_FILE_TYPES:
                				context = {
                    			
                    			'error_message': 'Image file must be PNG, JPG, or JPEG',
                			}
                				return render(request, 'Hostel/roomregistration.html', context)
            				roomregis.save()
            				#return HttpResponse('data stored in db')
				except:
					context = {
                    			
                    			'message': 'You have already registered for room',
                			}
					return render(request, 'Hostel/roomregistration.html', context)
    			else:
        			form = RoomRegistrationForm()
    		return render(request, 'Hostel/roomregistration.html', {
        'form': form
})
	else:
		context={'text':0}
		return render(request, 'Hostel/login.html',context)
def caretakerhostelcomplaint(request):
	k=len(HostelComplaint.objects.all())
	hostel_Complaint=[]
	student=[]
	complaint_time=[]
	
	hostelcomplaint_data=HostelComplaint.objects.all()
	room_regis=RoomRegistration.objects.all()
	for i in hostelcomplaint_data:
		for j in room_regis:
			if(i.student==j.student):
				
				hostel_Complaint.append(str(i.student))
				hostel_Complaint.append(str(i.complaint))
				hostel_Complaint.append(str(i.complain_time))
				hostel_Complaint.append(str(j.pref_room_no))
				hostel_Complaint.append(str(j.hostel_name))
				#hostel_Complaint.append("\n")
				#hostel_Complaint='\n'.join(hostel_Complaint)
		
	hostelcomplaint_data=HostelComplaint.objects.all().order_by('complain_time')
	
	context2={'hostel_complaint':hostel_Complaint}
	return render(request,'Hostel/caretakerhostelcomplaint.html',context2)
	

