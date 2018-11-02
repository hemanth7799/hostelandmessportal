from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.http import JsonResponse,HttpResponse
from django.shortcuts import render, get_object_or_404
from .forms import RefundForm,FeedbackForm
from django.contrib.auth import get_user_model
from Hostel.models  import Student
from Mess.models import Refund
User = get_user_model()

IMAGE_FILE_TYPES = ['png', 'jpg', 'jpeg','pdf']

def homepage(request):
	return render(request,'Mess/MyHome.html')
def messmenu(request):
	return render(request,'Mess/messmenu.html')
def refund(request):
    if not request.user.is_authenticated():
        return render(request, 'Mess/login.html')
    else:
        form = RefundForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            mess = form.save(commit=False)
            #mess.student = Student.objects.get(user=request.user)
	    usr=User.objects.get(username=request.user.username)
	    stud=Student()
	    stud=Student.objects.get(user=usr)
			
			

        		
            			
            from_date=request.POST.get('from_date')
	    to_date=request.POST.get('to_date')
				
	    messrefund=Refund()
	    messrefund.from_date=from_date
	    messrefund.mail_proof=request.FILES.get('mail_proof')
	    messrefund.to_date=to_date
	    messrefund.student=stud
           
            #mess.mail_proof = request.FILES['mail_proof']
            file_type = mess.mail_proof.url.split('.')[-1]
            file_type = file_type.lower()
            if file_type not in IMAGE_FILE_TYPES:
                context = {
                    #'mess': mess,
                    #'form': form,
                    'error_message': 'Image file must be PNG, JPG, or JPEG',
                }
                return render(request, 'Mess/refund.html', context)
            messrefund.save()
            return render(request, 'Mess/popup.html', {'error_message': 'refund form submitted successfully'})
        context = {
            "form": form,
        }
        return render(request, 'Mess/refund.html', context)


def feedback(request):
    if not request.user.is_authenticated():
        return render(request, 'Mess/login.html')
    else:
        form = FeedbackForm(request.POST or None)
        if form.is_valid():
            mess = form.save(commit=False)
            mess.student = Student.objects.get(user=request.user)
            mess.save()
            return render(request, 'Mess/popup.html', {'error_message': 'feedback submitted successfully'})
        context = {
            "form": form
        }
        return render(request, 'Mess/feedback.html', context)

import json
import requests
from django.shortcuts import get_object_or_404, render

def login(request,token):
    print ('hello')
    res = requests.post(url='https://serene-wildwood-35121.herokuapp.com/oauth/getDetails', data={
    'token': token,
    'secret': 'ff5bbfae032e66f2abdb15b113bfab5d3f1741b1ed1f60b04e7062d74024bad29f57b82e6cfe0eee53ee6e595405c00907af0179c85c2c0c396e6e3df1f250a7'
})
    res = json.loads(res.content)
    email = res['student'][0]['Student_Email']
    print(email)
    if(email):
        return render(request,'Mess/loginsuccess.html',{'email':email})

def login_user(request):
        return render(request,'Mess/login.html')



